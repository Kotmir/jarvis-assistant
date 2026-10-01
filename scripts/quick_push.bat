@echo off
REM JARVIS - Quick Push
REM Fork: KotMir based on https://github.com/RustamovAkrom/JARVIS

setlocal enabledelayedexpansion

if not exist .git exit /b 1

for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set BRANCH=%%i

REM Check arguments
if "%1"=="auto" (
    for /f "tokens=1-2 delims=/:" %%a in ('time /t') do set TIME=%%a:%%b
    set COMMIT_MSG=Auto [!TIME!] by KotMir
) else if not "%1"=="" (
    set COMMIT_MSG=%*
) else (
    echo Choose commit type:
    echo 1 = Auto (with time)
    echo 2 = Manual text
    echo.
    set /p CHOICE="Select [1-2]: "

    if "!CHOICE!"=="2" (
        set /p COMMIT_MSG="Commit message: "
    ) else (
        for /f "tokens=1-2 delims=/:" %%a in ('time /t') do set TIME=%%a:%%b
        set COMMIT_MSG=Auto [!TIME!] by KotMir
    )
)

cls
echo JARVIS Quick Push
echo Branch: %BRANCH%
echo Commit: %COMMIT_MSG%
echo.

git pull origin %BRANCH% 2>nul
git add -A
git commit -m "%COMMIT_MSG%" --no-verify 2>nul
git push origin %BRANCH%

echo.
echo Done!
pause
