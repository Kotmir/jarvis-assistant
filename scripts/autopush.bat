@echo off
REM J.A.R.V.I.S. Git AutoPush — батник для Windows
REM by KotMir — зелёный хакер в действии
REM
REM Использование:
REM   autopush.bat          — одна операция push
REM   autopush.bat daemon   — слушать изменения
REM   autopush.bat dry-run  — показать что будет

setlocal enabledelayedexpansion

set "INTERVAL=300"
set "MODE=once"

if "%1"=="daemon" (
    set "MODE=daemon"
    if not "%2"=="" set "INTERVAL=%2"
)
if "%1"=="dry-run" (
    python git_autopush.py --dry-run
    exit /b 0
)

if "%MODE%"=="daemon" (
    echo 🤖 Git AutoPush демон запущен (проверка каждые %INTERVAL% сек)
    echo Нажмите Ctrl+C для выхода
    echo.
    python git_autopush.py --daemon --interval %INTERVAL%
) else (
    python git_autopush.py --once
)
