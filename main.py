import sys
import os
import platform
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QListWidget, QListWidgetItem, QStackedWidget, QMessageBox, QLabel, 
                             QPushButton, QDialog, QTextEdit, QFrame)
from PyQt6.QtCore import QSize, Qt, QProcess
from PyQt6.QtGui import QIcon, QMouseEvent

import styles
from config import COLORS

# Importy stránek
from view_uninstaller import UninstallerPage
from view_installer import InstallerPage
from view_settings import SettingsPage
from view_health import HealthCheckPage
from view_updater import UpdaterPage
from splash import SplashScreen

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Mac nepotřebuje admin check pro Brew (naopak, Brew by neměl běžet pod rootem)
def check_brew():
    if platform.system() != "Darwin":
        return True # Ignorujeme na jiných OS pro teď
    
    # Rychlá kontrola existence brew
    if os.system("which brew > /dev/null 2>&1") != 0:
        return False
    return True

# --- HelpDialog zůstává stejný (zkráceno pro přehlednost) ---
class HelpDialog(QDialog):
    # ... (Zde nechte původní kód HelpDialogu, jen odstraňte Windows fonty jako Segoe MDL2)
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Univerzální aplikace (macOS)")
        self.resize(1150, 750)
        
        # Ikonka
        icon_path = resource_path("program_icon.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Na macOS nepoužíváme custom title bar hacky přes windll
        # Qt se postará o nativní vzhled

        try:
            self.setStyleSheet(styles.get_stylesheet())
        except Exception as e:
            print(f"Chyba stylů: {e}")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # LEVÝ PANEL (Sidebar)
        sidebar_container = QWidget()
        sidebar_container.setFixedWidth(260)
        sidebar_container.setStyleSheet(f"background-color: {COLORS['bg_sidebar']}; border-right: 1px solid {COLORS['border']};")
        
        sidebar_layout = QVBoxLayout(sidebar_container)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)

        self.sidebar_list = QListWidget()
        self.sidebar_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sidebar_list.setStyleSheet(f"""
            QListWidget {{ background-color: transparent; border: none; outline: none; margin-top: 10px; }}
            QListWidget::item {{ padding: 15px 10px; margin: 2px 10px; border-radius: 6px; color: {COLORS['sub_text']}; font-weight: 500; }}
            QListWidget::item:selected {{ background-color: {COLORS['item_bg']}; color: {COLORS['fg']}; border-left: 3px solid {COLORS['accent']}; }}
            QListWidget::item:hover {{ background-color: {COLORS['item_hover']}; color: {COLORS['fg']}; }}
        """)
        self.sidebar_list.currentRowChanged.connect(self.switch_main_page)
        
        self.add_sidebar_item("📦  Chytrá instalace")
        self.add_sidebar_item("🔄  Aktualizace")
        self.add_sidebar_item("🩺  Kontrola Macu")
        self.add_sidebar_item("🗑️  Odinstalace")
        
        sidebar_layout.addWidget(self.sidebar_list)
        sidebar_layout.addStretch()

        # Tlačítka dole
        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.setContentsMargins(15, 0, 15, 20)
        bottom_buttons_layout.setSpacing(10)

        self.btn_settings = QPushButton("⚙️ Nastavení")
        self.btn_settings.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_settings.setFixedHeight(40)
        self.btn_settings.clicked.connect(self.go_to_settings)
        self._style_bottom_btn(self.btn_settings)
        
        bottom_buttons_layout.addWidget(self.btn_settings)
        sidebar_layout.addLayout(bottom_buttons_layout)
        main_layout.addWidget(sidebar_container)

        # PRAVÝ OBSAH
        self.pages = QStackedWidget()
        main_layout.addWidget(self.pages)

        self.pages.addWidget(InstallerPage())          
        self.pages.addWidget(UpdaterPage())            
        self.pages.addWidget(HealthCheckPage())        
        self.pages.addWidget(UninstallerPage())    
        self.pages.addWidget(SettingsPage())           

        self.sidebar_list.setCurrentRow(0)

        if not check_brew():
            QMessageBox.critical(self, "Chyba", "Homebrew nebyl nalezen!\nProsím nainstalujte ho příkazem v terminálu:\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")

    def add_sidebar_item(self, text):
        item = QListWidgetItem(text)
        self.sidebar_list.addItem(item)

    def switch_main_page(self, index):
        if index >= 0:
            self.pages.setCurrentIndex(index)
            self._style_bottom_btn(self.btn_settings, active=False)

    def go_to_settings(self):
        self.sidebar_list.clearSelection()
        self.pages.setCurrentIndex(4)
        self._style_bottom_btn(self.btn_settings, active=True)

    def _style_bottom_btn(self, btn, active=False):
        bg_color = COLORS['item_bg'] if active else "transparent"
        border = f"1px solid {COLORS['accent']}" if active else "none"
        text_color = "white" if active else COLORS['sub_text']
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color}; color: {text_color}; border: {border};
                border-radius: 6px; font-weight: bold; text-align: center;
            }}
            QPushButton:hover {{ background-color: {COLORS['item_hover']}; color: white; }}
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 1. Vytvoříme instanci Splash Screenu
    splash = SplashScreen()
    
    # Proměnná pro hlavní okno (musí být definována v tomto scope)
    window = None

    # 2. Funkce, která se zavolá, až Splash Screen dokončí práci
    def show_main_window():
        global window 
        # Teprve teď vytvoříme hlavní okno (aby se nenačítalo zbytečně brzy)
        window = MainWindow()
        window.show()
        # Splash screen se sám zavře ve své metodě finish_loading(), 
        # takže ho tu nemusíme řešit.

    # 3. Propojíme signál 'finished' ze splashe s naší funkcí
    splash.finished.connect(show_main_window)

    # 4. Zobrazíme Splash Screen
    splash.show()

    sys.exit(app.exec())