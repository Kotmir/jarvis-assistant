@echo off
setlocal enabledelayedexpansion

cd /d "C:\Users\KotMir_You\Desktop\Jarvis-main"

echo.
echo ====================================
echo Reorganizing JARVIS structure...
echo ====================================
echo.

REM Create directories if they don't exist
if not exist "docs" mkdir docs
if not exist "scripts" mkdir scripts
if not exist "jarvis\ui" mkdir "jarvis\ui"

echo Moving documentation to docs/...
move "README_LIME_EDITION.md" "docs\" 2>nul
move "README_FORK_INFO.md" "docs\" 2>nul
move "SETUP_GUIDE.md" "docs\" 2>nul
move "THEME_CHANGES.md" "docs\" 2>nul
move "UPDATES.md" "docs\" 2>nul
move "BATCH_FILES_GUIDE.md" "docs\" 2>nul
move "QUICK_START.txt" "docs\" 2>nul
move "FINAL_SUMMARY.txt" "docs\" 2>nul

echo Moving batch files to scripts/...
move "autopush_simple.bat" "scripts\" 2>nul
move "quick_push.bat" "scripts\" 2>nul
move "update_and_push.bat" "scripts\" 2>nul
move "autopush.bat" "scripts\" 2>nul
move "install.bat" "scripts\" 2>nul
move "update.bat" "scripts\" 2>nul
move "run_jarvis.bat" "scripts\" 2>nul
move "run_jarvis_console.bat" "scripts\" 2>nul

echo Moving Python utilities to scripts/...
move "git_autopush.py" "scripts\" 2>nul

echo Moving theme to jarvis/ui/...
move "style_lime.py" "jarvis\ui\" 2>nul

echo.
echo ====================================
echo Done! Files organized.
echo ====================================
echo.
echo Root directory now contains:
dir /ad /b
echo.
pause
