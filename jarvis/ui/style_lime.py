"""Тема JARVIS: лайм-хакер. Неоновая зелень #00ff00, тёмный фон, киберпанк-стиль.

   by KotMir — настоящий хакер-шик с лайм-свечением и матричным эффектом.
"""

ACCENT = "#00ff00"  # 🟢 Лайм-зелень
SECONDARY = "#00cc00"  # Тёмнее
HIGHLIGHT = "#ffff00"  # Жёлтый акцент
DANGER = "#ff0055"  # Красный для ошибок
MONO = "'Cascadia Mono', 'Courier New', monospace"

QSS = """
* { font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif; color: #00ff00; }
QMainWindow { background: #0a0e1a; }
QToolTip { background: #0f1620; color: #00ff00; border: 2px solid #00ff00; padding: 5px 8px; border-radius: 3px; }

/* ---------- шапка: НЕОНОВАЯ ЗЕЛЕНЬ ---------- */
#brand { font-size: 20px; font-weight: 900; letter-spacing: 7px; color: #00ff00; text-shadow: 0 0 10px #00ff00; }
#brandState { font-size: 12px; font-weight: 900; letter-spacing: 4px; color: #00ff00; }
#brandState[state="listening"] { color: #ffff00; text-shadow: 0 0 8px #ffff00; }
#brandState[state="thinking"] { color: #00ff00; text-shadow: 0 0 8px #00ff00; }
#brandState[state="executing"] { color: #00ccff; text-shadow: 0 0 8px #00ccff; }
#brandState[state="speaking"] { color: #ffff00; text-shadow: 0 0 8px #ffff00; }
#brandState[state="error"] { color: #ff0055; text-shadow: 0 0 10px #ff0055; }
#personality { font-size: 12px; color: #00cc00; letter-spacing: 1px; }
#clock { font-family: """ + MONO + """; font-size: 18px; color: #00ff00; letter-spacing: 2px; font-weight: 700; }
#date { font-size: 10px; color: #007700; letter-spacing: 2px; }
QPushButton#iconBtn {
    background: rgba(0, 255, 0, 0.08); border: 2px solid #00ff00; border-radius: 15px;
    min-width: 30px; max-width: 30px; min-height: 30px; max-height: 30px; padding: 0; font-size: 14px;
}
QPushButton#iconBtn:hover { background: rgba(0, 255, 0, 0.2); box-shadow: 0 0 10px #00ff00; }

/* ---------- панели: МАТРИЧНЫЙ СТИЛЬ ---------- */
#hudPanel { background: rgba(10, 14, 26, 0.9); border: 2px solid #00ff00; border-radius: 5px; box-shadow: 0 0 8px rgba(0, 255, 0, 0.3); }
#panelTitle { font-size: 10px; font-weight: 900; letter-spacing: 4px; color: #00ff00; text-shadow: 0 0 5px #00ff00; }
#metricName { font-size: 10px; font-weight: 700; letter-spacing: 2px; color: #007700; }
#metricValue { font-family: """ + MONO + """; font-size: 12px; color: #00ff00; font-weight: 700; }
#metricValue[na="true"] { color: #004400; }
#dot { font-size: 11px; color: #003300; }
#dot[ok="true"] { color: #00ff00; text-shadow: 0 0 5px #00ff00; }
#dot[ok="false"] { color: #ff0055; text-shadow: 0 0 5px #ff0055; }
QProgressBar#bar { background: rgba(0, 255, 0, 0.05); border: 1px solid #00ff00; border-radius: 2px; max-height: 4px; }
QProgressBar#bar::chunk { border-radius: 2px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00cc00, stop:1 #00ff00); box-shadow: 0 0 5px #00ff00; }
QProgressBar#bar[hot="true"]::chunk { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff6600, stop:1 #ff0055); }

/* ---------- центр: КИБЕРПАНК ---------- */
#caption { font-size: 15px; color: #00ff00; font-style: italic; font-weight: 700; text-shadow: 0 0 5px #00ff00; }
#subcaption { font-size: 11px; color: #007700; letter-spacing: 1px; }
QPushButton#quick {
    background: rgba(0, 255, 0, 0.06); border: 2px solid #00ff00; border-radius: 5px;
    padding: 7px 10px; font-size: 10px; font-weight: 900; letter-spacing: 2px; color: #00ff00;
}
QPushButton#quick:hover { background: rgba(0, 255, 0, 0.15); color: #ffff00; text-shadow: 0 0 5px #ffff00; box-shadow: 0 0 8px #00ff00; }
QPushButton#quick:pressed { background: rgba(0, 255, 0, 0.25); }

/* ---------- лента событий: ЛОГИ ---------- */
QScrollArea { background: transparent; border: none; }
QScrollArea > QWidget > QWidget { background: transparent; }
#leftColumn { background: transparent; }
#timelineInner { background: transparent; }
QScrollBar:vertical { background: transparent; width: 6px; margin: 2px 0; }
QScrollBar::handle:vertical { background: #00ff00; border-radius: 3px; min-height: 30px; box-shadow: 0 0 5px #00ff00; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }
#evTime { font-family: """ + MONO + """; font-size: 10px; color: #004400; }
#evTag { font-size: 9px; font-weight: 900; letter-spacing: 2px; padding: 1px 6px; border-radius: 2px; }
#evTag[kind="voice"] { color: #ffff00; background: rgba(255, 255, 0, 0.10); border: 1px solid #ffff00; }
#evTag[kind="ai"] { color: #00ff00; background: rgba(0, 255, 0, 0.10); border: 1px solid #00ff00; }
#evTag[kind="tool"] { color: #00ccff; background: rgba(0, 204, 255, 0.10); border: 1px solid #00ccff; }
#evTag[kind="system"] { color: #00ff00; background: rgba(0, 255, 0, 0.08); border: 1px solid #00ff00; }
#evTag[kind="success"] { color: #00ff00; background: rgba(0, 255, 0, 0.10); border: 1px solid #00ff00; }
#evTag[kind="error"] { color: #ff0055; background: rgba(255, 0, 85, 0.10); border: 1px solid #ff0055; }
#evText { font-size: 12px; color: #00ff00; }
#evText[kind="ai"] { color: #00ff00; }
#evText[kind="error"] { color: #ff0055; }
#evText[kind="system"] { color: #00cc00; }
#evRow { border-left: 2px solid #00ff00; }

/* ---------- командная строка: ХАКЕР-СТИЛЬ ---------- */
#commandBar { background: rgba(10, 14, 26, 0.95); border: 2px solid #00ff00; border-radius: 5px; box-shadow: 0 0 15px rgba(0, 255, 0, 0.4); }
#prompt { font-family: """ + MONO + """; font-size: 16px; color: #00ff00; font-weight: 900; }
QLineEdit#command {
    background: transparent; border: none; font-family: """ + MONO + """; font-size: 14px; color: #00ff00;
    selection-background-color: rgba(0, 255, 0, 0.2); font-weight: 700;
}
QPushButton#mic {
    border-radius: 20px; min-width: 40px; max-width: 40px; min-height: 40px; max-height: 40px; padding: 0;
    font-size: 17px; background: rgba(0, 255, 0, 0.1); border: 2px solid #00ff00;
}
QPushButton#mic:hover { background: rgba(0, 255, 0, 0.2); box-shadow: 0 0 10px #00ff00; }
QPushButton#mic[active="true"] { background: rgba(255, 255, 0, 0.25); border: 2px solid #ffff00; box-shadow: 0 0 12px #ffff00; }
QPushButton#send {
    background: rgba(0, 255, 0, 0.12); border: 2px solid #00ff00; border-radius: 5px;
    padding: 7px 16px; font-size: 10px; font-weight: 900; letter-spacing: 3px; color: #00ff00;
}
QPushButton#send:hover { background: rgba(0, 255, 0, 0.25); box-shadow: 0 0 10px #00ff00; }
QPushButton#toggle {
    background: transparent; border: 2px solid #00ff00; border-radius: 5px; padding: 4px 9px;
    font-size: 9px; font-weight: 900; letter-spacing: 2px; color: #007700;
}
QPushButton#toggle:checked { color: #ffff00; border-color: #ffff00; background: rgba(255, 255, 0, 0.08); box-shadow: 0 0 8px #ffff00; }

#confirmBar { background: rgba(85, 60, 0, 0.9); border: 2px solid #ff6600; border-radius: 5px; }
#confirmText { color: #ffff00; font-size: 13px; font-weight: 700; }
QPushButton#yes { background: rgba(0, 255, 0, 0.25); border: 2px solid #00ff00; border-radius: 5px; padding: 6px 14px; }
QPushButton#no { background: rgba(255, 0, 85, 0.25); border: 2px solid #ff0055; border-radius: 5px; padding: 6px 14px; }

/* ---------- уведомления: ГРОМКИЕ ---------- */
#toast, #overlayToast {
    background: rgba(10, 14, 26, 0.95); border: 2px solid #00ff00; border-radius: 5px;
    padding: 7px 14px; font-size: 10px; font-weight: 900; letter-spacing: 2px; color: #00ff00; box-shadow: 0 0 10px #00ff00;
}
#toast[kind="error"], #overlayToast[kind="error"] { border-color: #ff0055; color: #ff0055; box-shadow: 0 0 10px #ff0055; }
#toast[kind="success"], #overlayToast[kind="success"] { border-color: #00ff00; color: #00ff00; box-shadow: 0 0 10px #00ff00; }

/* ---------- меню / настройки: СТИЛЬ ---------- */
QMenu { background: #0a0e1a; border: 2px solid #00ff00; border-radius: 5px; padding: 5px; }
QMenu::item { padding: 6px 22px 6px 14px; border-radius: 3px; font-size: 12px; color: #00ff00; }
QMenu::item:selected { background: rgba(0, 255, 0, 0.2); }
QMenu::separator { height: 1px; background: #00ff00; margin: 4px 8px; }
QMenu::indicator { width: 12px; height: 12px; }
QDialog { background: #0a0e1a; }
#settingsSection { font-size: 10px; font-weight: 900; letter-spacing: 4px; color: #00ff00; padding-top: 8px; text-shadow: 0 0 5px #00ff00; }
QCheckBox { font-size: 12px; color: #00ff00; spacing: 10px; }
QCheckBox::indicator { width: 32px; height: 16px; border-radius: 8px; background: #0a0e1a; border: 2px solid #00ff00; }
QCheckBox::indicator:checked { background: #00ff00; border: 2px solid #00ff00; }
QComboBox {
    background: #0a0e1a; border: 2px solid #00ff00; border-radius: 5px; padding: 5px 10px; font-size: 12px; color: #00ff00;
}
QComboBox:hover { border-color: #ffff00; box-shadow: 0 0 5px #ffff00; }
QComboBox QAbstractItemView { background: #0a0e1a; selection-background-color: rgba(0, 255, 0, 0.2); border: 2px solid #00ff00; }
QSlider::groove:horizontal { height: 4px; background: #002200; border-radius: 2px; }
QSlider::sub-page:horizontal { background: #00ff00; border-radius: 2px; box-shadow: 0 0 5px #00ff00; }
QSlider::handle:horizontal { width: 14px; height: 14px; margin: -6px 0; border-radius: 7px; background: #00ff00; box-shadow: 0 0 5px #00ff00; }
QPushButton {
    background: rgba(0, 255, 0, 0.08); border: 2px solid #00ff00; border-radius: 5px; padding: 6px 14px;
    font-size: 12px; color: #00ff00; font-weight: 700;
}
QPushButton:hover { background: rgba(0, 255, 0, 0.18); box-shadow: 0 0 8px #00ff00; }
QProgressBar#micMeter { background: #0a0e1a; border: 2px solid #00ff00; border-radius: 3px; max-height: 6px; }
QProgressBar#micMeter::chunk { background: #00ff00; border-radius: 3px; box-shadow: 0 0 5px #00ff00; }
"""
