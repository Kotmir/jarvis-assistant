@echo off
REM JARVIS - Simple AutoPush
REM Fork: KotMir based on https://github.com/RustamovAkrom/JARVIS
REM Simple: just pull + add + commit + push

setlocal enabledelayedexpansion

if not exist .git exit /b 1

for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set BRANCH=%%i
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do set TIME=%%a:%%b

set COMMIT_MSG=Auto commit [!TIME!] by KotMir

git pull origin %BRANCH% >nul 2>&1
git add -A
git commit -m "%COMMIT_MSG%" --no-verify >nul 2>&1
git push origin %BRANCH%

echo Done: %COMMIT_MSG%
