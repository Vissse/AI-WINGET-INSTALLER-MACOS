import subprocess
import json
import re
import platform
from PyQt6.QtCore import QThread, pyqtSignal

class WingetListWorker(QThread):
    finished = pyqtSignal(list)
    error = pyqtSignal(str)

    def run(self):
        # --- ČÁST PRO WINDOWS (VÝVOJ) ---
        # Pokud nejsme na Macu (Darwin), vrátíme jen testovací data, aby aplikace nespadla.
        if platform.system() != "Darwin":
            print("Detekován Windows -> Vracím testovací data pro Mac...")
            mock_apps = [
                {'name': 'Google Chrome (Test)', 'id': 'google-chrome'},
                {'name': 'Visual Studio Code (Test)', 'id': 'visual-studio-code'},
                {'name': 'VLC Player (Test)', 'id': 'vlc'},
                {'name': 'Spotify (Test)', 'id': 'spotify'}
            ]
            self.finished.emit(mock_apps)
            return

        # --- ČÁST PRO MACOS (OSTRÝ PROVOZ) ---
        try:
            # Homebrew příkaz pro výpis verzí
            result = subprocess.run(
                ['brew', 'list', '--cask', '--versions'],
                capture_output=True, text=True
            )
            
            apps = []
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if not line: continue
                    # Format výstupu brew: "google-chrome 120.0.6099.109"
                    parts = line.split()
                    if len(parts) >= 1:
                        app_id = parts[0]
                        # Pro hezčí jméno nahradíme pomlčky mezerami a zvětšíme písmena
                        name = app_id.replace('-', ' ').title()
                        apps.append({'name': name, 'id': app_id})
            
            apps.sort(key=lambda x: x['name'].lower())
            self.finished.emit(apps)

        except Exception as e:
            self.error.emit(str(e))

class UninstallWorker(QThread):
    log = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, app_id):
        super().__init__()
        self.app_id = app_id

    def run(self):
        self.log.emit(f"Spouštím odinstalaci: {self.app_id}")
        
        # --zap smaže i konfigurační soubory (clean uninstall)
        cmd = ['brew', 'uninstall', '--zap', self.app_id]
        
        try:
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                text=True
            )
            
            for line in process.stdout:
                self.log.emit(line.strip())
                
            process.wait()
            
            if process.returncode == 0:
                self.log.emit("✅ Úspěšně odinstalováno.")
            else:
                self.log.emit("⚠️ Odinstalace skončila s varováním (nebo aplikace nebyla nalezena).")
                
        except Exception as e:
            self.log.emit(f"❌ Chyba procesu: {e}")

        self.finished.emit()