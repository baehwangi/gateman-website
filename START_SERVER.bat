@echo off
cd /d "%~dp0"
cls
echo.
echo ============================================================
echo   GATEMAN Web Server
echo ============================================================
echo.
echo Starting server...
echo.
node server.js
pause
