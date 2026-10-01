@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0"

if not exist ".git" (
    echo ERROR: No .git repository found!
    echo Make sure you're in the JARVIS root directory
    pause
    exit /b 1
)

if exist "scripts\quick_push.bat" (
    call scripts\quick_push.bat %*
) else (
    echo ERROR: scripts\quick_push.bat not found!
    pause
    exit /b 1
)
