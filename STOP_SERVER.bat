@echo off
echo Stopping all Node.js servers...
taskkill /F /IM node.exe >nul 2>&1
if %errorlevel% equ 0 (
    echo Server stopped successfully!
) else (
    echo No server was running.
)
echo.
pause
