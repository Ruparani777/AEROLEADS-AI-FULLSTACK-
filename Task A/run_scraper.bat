@echo off
echo ======================================================================
echo LinkedIn Profile Scraper - Starting...
echo ======================================================================
echo.

python linkedin_scraper.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Python command failed. Trying 'py' instead...
    py linkedin_scraper.py
)

echo.
echo ======================================================================
echo Press any key to close this window...
pause >nul
