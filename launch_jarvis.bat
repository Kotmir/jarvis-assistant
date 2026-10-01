@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0"

echo.
echo ====================================
echo Launching J.A.R.V.I.S.
echo Lime Hacker Edition by KotMir
echo ====================================
echo.

if not exist "main.py" (
    echo ERROR: main.py not found!
    echo Make sure you're in the JARVIS root directory
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ERROR: requirements.txt not found!
    pause
    exit /b 1
)

echo Checking dependencies...
python -c "import PySide6" >nul 2>&1

if %errorlevel% neq 0 (
    echo.
    echo Installing dependencies...
    echo This may take a few minutes...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ERROR: Failed to install dependencies
        echo Try running manually: pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo.
    echo Dependencies installed successfully!
    echo.
)

echo Starting JARVIS...
echo.

python main.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to start JARVIS
    pause
    exit /b 1
)
