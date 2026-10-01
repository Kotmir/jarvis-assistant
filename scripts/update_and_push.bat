@echo off
setlocal enabledelayedexpansion

REM JARVIS - Update and Push
REM Fork: KotMir based on https://github.com/RustamovAkrom/JARVIS

cls
echo =========================================
echo JARVIS - Update and Push by KotMir
echo =========================================
echo.

if not exist .git (
    echo ERROR: No .git repository found!
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set BRANCH=%%i

if not defined BRANCH (
    echo ERROR: Cannot determine current branch
    pause
    exit /b 1
)

echo Branch: %BRANCH%
echo.

REM STEP 1: Pull
echo [1/4] Pulling changes...
git pull origin %BRANCH% 2>nul
if %errorlevel% neq 0 (
    echo WARNING: Pull failed or already up to date
)
echo Done.
echo.

REM STEP 2: Check changes
echo [2/4] Checking for changes...
git status --porcelain >nul
if %errorlevel% neq 0 (
    echo ERROR: Status check failed
    pause
    exit /b 1
)

for /f %%a in ('git status --porcelain ^| find /c /v ""') do set CHANGES=%%a

if %CHANGES% equ 0 (
    echo No changes to commit.
    echo.
    echo Everything is up to date!
    pause
    exit /b 0
)

echo Found %CHANGES% changes.
echo.

REM STEP 3: Choose commit message
echo [3/4] Select commit message:
echo.
echo   1 = I will type my own text
echo   2 = Auto message with time
echo   3 = Cancel
echo.
set /p CHOICE="Choose [1-3]: "

if "%CHOICE%"=="3" (
    echo Cancelled.
    exit /b 0
)

if "%CHOICE%"=="1" (
    echo.
    set /p COMMIT_MSG="Enter commit message: "
    if "!COMMIT_MSG!"=="" (
        echo ERROR: Message cannot be empty
        pause
        exit /b 1
    )
) else if "%CHOICE%"=="2" (
    for /f "tokens=1-2 delims=/:" %%a in ('time /t') do set TIME=%%a:%%b
    set COMMIT_MSG=Auto update [!TIME!] by KotMir
) else (
    echo ERROR: Invalid choice
    pause
    exit /b 1
)

cls
echo =========================================
echo JARVIS - Update and Push by KotMir
echo =========================================
echo.
echo Branch: %BRANCH%
echo Commit: %COMMIT_MSG%
echo.

REM STEP 4: Add files
echo [1/4] Adding files...
git add -A
echo Done.
echo.

REM STEP 5: Commit
echo [2/4] Creating commit...
git commit -m "%COMMIT_MSG%" --no-verify 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Commit failed
    pause
    exit /b 1
)
echo Done: %COMMIT_MSG%
echo.

REM STEP 6: Push
echo [3/4] Pushing to GitHub...
git push origin %BRANCH%
if %errorlevel% neq 0 (
    echo ERROR: Push failed. Check internet connection.
    pause
    exit /b 1
)
echo Done.
echo.

REM Done
echo =========================================
echo SUCCESS! All done!
echo Commit: %COMMIT_MSG%
echo Branch: %BRANCH%
echo Check GitHub for new commit!
echo =========================================
echo.

pause
