# presets.py

# ==============================================================================
# 1. DEFINICE JEDNOTLIVÝCH APLIKACÍ (S IKONAMI)
# ==============================================================================

# Používáme repozitář dashboard-icons přes jsDelivr
BASE_ICON_URL = "https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png"

# --- Herní Launchery ---
steam_app = {
    "name": "Steam", "id": "steam", "website": "https://store.steampowered.com",
    "icon_url": f"{BASE_ICON_URL}/steam.png"
}
epic_app = {
    "name": "Epic Games Launcher", "id": "epic-games", "website": "https://store.epicgames.com",
    "icon_url": f"{BASE_ICON_URL}/epic-games.png"
}
ubisoft_app = {
    "name": "Ubisoft Connect", "id": "ubisoft-connect", "website": "https://ubisoftconnect.com",
    "icon_url": f"{BASE_ICON_URL}/ubisoft-connect.png"
}
ea_app = {
    "name": "EA App", "id": "ea", "website": "https://www.ea.com/ea-app",
    "icon_url": f"{BASE_ICON_URL}/ea.png"
}
gog_app = {
    "name": "GOG GALAXY", "id": "gog-galaxy", "website": "https://www.gog.com/galaxy",
    "icon_url": f"{BASE_ICON_URL}/gog-galaxy.png"
}
# Playnite na Macu není -> Nahrazeno/Zakomentováno
battlenet_app = {
    "name": "Battle.net", "id": "battle-net", "website": "https://www.blizzard.com",
    "icon_url": f"{BASE_ICON_URL}/battle-net.png"
}
curseforge_app = {
    "name": "CurseForge", "id": "curseforge", "website": "https://www.curseforge.com",
    "icon_url": f"{BASE_ICON_URL}/curseforge.png"
}
riot_app = {
    "name": "Riot Client", "id": "riot-client", "website": "https://www.riotgames.com",
    "icon_url": f"{BASE_ICON_URL}/riot-games.png"
}
# Wargaming Game Center je na Macu problematický přes Cask, ale existuje

# --- Prohlížeče ---
chrome_app = {
    "name": "Google Chrome", "id": "google-chrome", "website": "https://www.google.com/chrome",
    "icon_url": f"{BASE_ICON_URL}/google-chrome.png"
}
firefox_app = {
    "name": "Mozilla Firefox", "id": "firefox", "website": "https://www.mozilla.org/firefox",
    "icon_url": f"{BASE_ICON_URL}/firefox.png"
}
edge_app = {
    "name": "Microsoft Edge", "id": "microsoft-edge", "website": "https://www.microsoft.com/edge",
    "icon_url": f"{BASE_ICON_URL}/microsoft-edge.png"
}
brave_app = {
    "name": "Brave Browser", "id": "brave-browser", "website": "https://brave.com",
    "icon_url": f"{BASE_ICON_URL}/brave.png"
}
opera_app = {
    "name": "Opera", "id": "opera", "website": "https://www.opera.com",
    "icon_url": f"{BASE_ICON_URL}/opera.png"
}
opera_gx_app = {
    "name": "Opera GX", "id": "opera-gx", "website": "https://www.opera.com/gx",
    "icon_url": f"{BASE_ICON_URL}/opera-gx.png"
}
vivaldi_app = {
    "name": "Vivaldi", "id": "vivaldi", "website": "https://vivaldi.com",
    "icon_url": f"{BASE_ICON_URL}/vivaldi.png"
}
zen_app = {
    "name": "Zen Browser", "id": "zen-browser", "website": "https://www.zen-browser.app",
    "icon_url": "https://cdn.jsdelivr.net/gh/zen-browser/desktop/assets/zen-logo.png" 
}
librewolf_app = {
    "name": "LibreWolf", "id": "librewolf", "website": "https://librewolf.net",
    "icon_url": f"{BASE_ICON_URL}/librewolf.png"
}
ungoogled_app = {
    "name": "Ungoogled Chromium", "id": "eloston-chromium", "website": "https://github.com/ungoogled-software/ungoogled-chromium",
    "icon_url": f"{BASE_ICON_URL}/ungoogled-chromium.png"
}
waterfox_app = {
    "name": "Waterfox", "id": "waterfox", "website": "https://www.waterfox.net",
    "icon_url": f"{BASE_ICON_URL}/waterfox.png"
}

# --- Komunikace ---
discord_app = {
    "name": "Discord", "id": "discord", "website": "https://discord.com",
    "icon_url": f"{BASE_ICON_URL}/discord.png"
}
telegram_app = {
    "name": "Telegram", "id": "telegram", "website": "https://desktop.telegram.org",
    "icon_url": f"{BASE_ICON_URL}/telegram.png"
}
signal_app = {
    "name": "Signal", "id": "signal", "website": "https://signal.org",
    "icon_url": f"{BASE_ICON_URL}/signal.png"
}
teams_app = {
    "name": "Microsoft Teams", "id": "microsoft-teams", "website": "https://www.microsoft.com/microsoft-teams",
    "icon_url": f"{BASE_ICON_URL}/microsoft-teams.png"
}
skype_app = {
    "name": "Skype", "id": "skype", "website": "https://www.skype.com",
    "icon_url": f"{BASE_ICON_URL}/skype.png"
}

# --- Grafika ---
gimp_app = {
    "name": "GIMP", "id": "gimp", "website": "https://www.gimp.org",
    "icon_url": f"{BASE_ICON_URL}/gimp.png"
}
# Paint.NET je Windows only -> Nahrazeno Seashore (Mac native simple editor)
seashore_app = {
    "name": "Seashore", "id": "seashore", "website": "https://github.com/robaho/seashore",
    "icon_url": "https://upload.wikimedia.org/wikipedia/commons/9/94/Seashore_Icon.png"
}
inkscape_app = {
    "name": "Inkscape", "id": "inkscape", "website": "https://inkscape.org",
    "icon_url": f"{BASE_ICON_URL}/inkscape.png"
}
krita_app = {
    "name": "Krita", "id": "krita", "website": "https://krita.org",
    "icon_url": f"{BASE_ICON_URL}/krita.png"
}
blender_app = {
    "name": "Blender", "id": "blender", "website": "https://www.blender.org",
    "icon_url": f"{BASE_ICON_URL}/blender.png"
}
# IrfanView je Windows only -> XnViewMP je dobrá alternativa pro Mac
xnview_app = {
    "name": "XnView MP", "id": "xnviewmp", "website": "https://www.xnview.com",
    "icon_url": f"{BASE_ICON_URL}/xnview-mp.png"
}
affinity_app = {
    "name": "Affinity", "id": "affinity", "website": "https://affinity.serif.com",
    "icon_url": f"{BASE_ICON_URL}/affinity.png" 
}

# --- Video ---
vlc_app = {
    "name": "VLC media player", "id": "vlc", "website": "https://www.videolan.org/vlc",
    "icon_url": f"{BASE_ICON_URL}/vlc.png"
}
# MPC-BE a PotPlayer jsou Windows only -> IINA je nejlepší přehrávač pro Mac
iina_app = {
    "name": "IINA", "id": "iina", "website": "https://iina.io",
    "icon_url": "https://iina.io/images/iina-icon-60.png"
}
kodi_app = {
    "name": "Kodi", "id": "kodi", "website": "https://kodi.tv",
    "icon_url": f"{BASE_ICON_URL}/kodi.png"
}

# --- Nástroje (Archivátory a editory) ---
# WinRAR na Macu nemá GUI verzi zdarma stejnou jako na Win. Používá se Keka nebo The Unarchiver.
keka_app = {
    "name": "Keka", "id": "keka", "website": "https://www.keka.io",
    "icon_url": f"{BASE_ICON_URL}/keka.png"
}
unarchiver_app = {
    "name": "The Unarchiver", "id": "the-unarchiver", "website": "https://theunarchiver.com",
    "icon_url": "https://upload.wikimedia.org/wikipedia/en/3/30/The_Unarchiver_icon.png"
}

# --- Audio ---
audacity_app = {
    "name": "Audacity", "id": "audacity", "website": "https://www.audacityteam.org",
    "icon_url": f"{BASE_ICON_URL}/audacity.png"
}
ocenaudio_app = {
    "name": "ocenaudio", "id": "ocenaudio", "website": "https://www.ocenaudio.com",
    "icon_url": f"{BASE_ICON_URL}/ocenaudio.png"
}

# ==============================================================================
# 2. DEFINICE SKUPIN (SOUHRNNÉ LISTY)
# ==============================================================================

_BROWSERS = [chrome_app, firefox_app, edge_app, brave_app, opera_app, opera_gx_app, vivaldi_app, zen_app, librewolf_app, ungoogled_app, waterfox_app]
_CHAT = [discord_app, telegram_app, signal_app, teams_app, skype_app]
_GAMES = [steam_app, epic_app, ubisoft_app, ea_app, gog_app, battlenet_app, riot_app, curseforge_app]
_GRAPHICS = [gimp_app, seashore_app, inkscape_app, krita_app, blender_app, xnview_app, affinity_app]
_VIDEO = [vlc_app, iina_app, kodi_app]
_AUDIO = [audacity_app, ocenaudio_app]

_PDF = [
    {"name": "Adobe Acrobat Reader", "id": "adobe-acrobat-reader", "website": "https://get.adobe.com/reader", "icon_url": f"{BASE_ICON_URL}/adobe-acrobat-reader.png"},
    # Sumatra neexistuje na Macu, Preview (náhled) je built-in
    {"name": "Foxit PDF Editor", "id": "foxit-pdf-editor", "website": "https://www.foxit.com", "icon_url": f"{BASE_ICON_URL}/foxit-reader.png"}
]

_OFFICE = [
    {"name": "LibreOffice", "id": "libreoffice", "website": "https://www.libreoffice.org", "icon_url": f"{BASE_ICON_URL}/libreoffice.png"},
    {"name": "Microsoft 365 (Office)", "id": "microsoft-office", "website": "https://www.office.com", "icon_url": f"{BASE_ICON_URL}/microsoft-office.png"},
    {"name": "OnlyOffice", "id": "onlyoffice", "website": "https://www.onlyoffice.com", "icon_url": f"{BASE_ICON_URL}/onlyoffice.png"}
]

_TOOLS = [
    keka_app,
    unarchiver_app,
    # Notepad++ je Windows only -> CotEditor je skvělý Mac editor
    {"name": "CotEditor", "id": "coteditor", "website": "https://coteditor.com", "icon_url": "https://coteditor.com/img/appicon/512@2x.png"},
    {"name": "Sublime Text", "id": "sublime-text", "website": "https://www.sublimetext.com", "icon_url": f"{BASE_ICON_URL}/sublime-text.png"},
    {"name": "AnyDesk", "id": "anydesk", "website": "https://anydesk.com", "icon_url": f"{BASE_ICON_URL}/anydesk.png"},
    {"name": "OBS Studio", "id": "obs", "website": "https://obsproject.com", "icon_url": f"{BASE_ICON_URL}/obs-studio.png"},
    # PowerToys není na Macu, Raycast je dobrá alternativa
    {"name": "Raycast", "id": "raycast", "website": "https://www.raycast.com", "icon_url": f"{BASE_ICON_URL}/raycast.png"}
]

_DEV = [
    {"name": "VS Code", "id": "visual-studio-code", "website": "https://code.visualstudio.com", "icon_url": f"{BASE_ICON_URL}/visual-studio-code.png"},
    # Git a Python jsou v Brew jako "Formulae", ne "Casks". Aplikace instaluje Casks. 
    # VS Code je Cask, takže funguje.
    {"name": "iTerm2", "id": "iterm2", "website": "https://iterm2.com", "icon_url": f"{BASE_ICON_URL}/iterm.png"},
    {"name": "Docker", "id": "docker", "website": "https://www.docker.com", "icon_url": f"{BASE_ICON_URL}/docker.png"}
]


# ==============================================================================
# 3. MAPOVÁNÍ KLÍČOVÝCH SLOV (PRESETS)
# ==============================================================================

PRESETS = {
    # === SEKTOR: HRY (GAMING) ===
    "hry": _GAMES,
    "hra": _GAMES,
    "games": _GAMES,
    "gaming": _GAMES,
    "launchers": _GAMES,
    # Konkrétní
    "steam": [steam_app],
    "epic": [epic_app],
    "ubisoft": [ubisoft_app],
    "ea": [ea_app],
    "gog": [gog_app],
    "battlenet": [battlenet_app],
    "blizzard": [battlenet_app],
    "riot": [riot_app],
    "lol": [riot_app],
    "curseforge": [curseforge_app],

    # === SEKTOR: INTERNET & PROHLÍŽEČE ===
    "prohlížeč": _BROWSERS,
    "browser": _BROWSERS,
    "internet": _BROWSERS,
    "web": _BROWSERS,
    # Konkrétní
    "chrome": [chrome_app],
    "firefox": [firefox_app],
    "edge": [edge_app],
    "opera": [opera_app],
    "gx": [opera_gx_app],       
    "opera gx": [opera_gx_app], 
    "brave": [brave_app],
    "vivaldi": [vivaldi_app],
    "zen": [zen_app],
    "librewolf": [librewolf_app], 
    "ungoogled": [ungoogled_app], 
    "chromium": [ungoogled_app],  
    "waterfox": [waterfox_app],   

    # === SEKTOR: KOMUNIKACE ===
    "chat": _CHAT,
    "komunikace": _CHAT,
    "messenger": _CHAT,
    "social": _CHAT,
    # Konkrétní
    "discord": [discord_app],
    "telegram": [telegram_app],
    "teams": [teams_app],
    "skype": [skype_app],
    "signal": [signal_app],

    # === SEKTOR: VIDEO & PŘEHRÁVAČE ===
    "video": _VIDEO,
    "přehrávač": _VIDEO,
    "player": _VIDEO,
    "filmy": _VIDEO,
    # Konkrétní
    "vlc": [vlc_app],
    "iina": [iina_app],
    "potplayer": [iina_app], # Mapping PotPlayeru na IINA (alternativa)
    "mpc": [iina_app],       # Mapping MPC na IINA
    "kodi": [kodi_app],

    # === SEKTOR: GRAFIKA & KREATIVITA ===
    "grafika": _GRAPHICS,
    "foto": _GRAPHICS,
    "design": _GRAPHICS,
    # Konkrétní
    "gimp": [gimp_app],
    "paint": [seashore_app], 
    "krita": [krita_app],
    "blender": [blender_app],
    "irfan": [xnview_app],
    "affinity": [affinity_app], 

    # === SEKTOR: KANCELÁŘ ===
    "office": _OFFICE,
    "kancelář": _OFFICE,
    "dokumenty": _OFFICE,
    "pdf": _PDF,
    "reader": _PDF,
    # Konkrétní
    "word": _OFFICE,
    "excel": _OFFICE,

    # === SEKTOR: SYSTÉMOVÉ NÁSTROJE ===
    "tools": _TOOLS,
    "nástroje": _TOOLS,
    "utility": _TOOLS,
    "zip": [keka_app, unarchiver_app],
    "rar": [keka_app, unarchiver_app],
    # Konkrétní
    "winrar": [keka_app], # WinRAR -> Keka
    "7zip": [keka_app], 
    "anydesk": [_TOOLS[4]],
    "raycast": [_TOOLS[6]],
    
    # === SEKTOR: VÝVOJ ===
    "dev": _DEV,
    "vývoj": _DEV,
    "programování": _DEV,
    # Konkrétní
    "vscode": [_DEV[0]],
    "iterm": [_DEV[1]],
    "docker": [_DEV[2]],

    # === SEKTOR: AUDIO & ZVUK ===
    "audio": _AUDIO,
    "zvuk": _AUDIO,
    "sound": _AUDIO,
    "editor zvuku": _AUDIO,
    # Konkrétní
    "audacity": [audacity_app],
    "ocenaudio": [ocenaudio_app]
}