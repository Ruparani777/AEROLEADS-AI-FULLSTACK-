@echo off
echo ======================================================================
echo Installing LinkedIn Scraper Dependencies
echo ======================================================================
echo.
echo This may take 1-2 minutes...
echo.

python -m pip install --upgrade pip
python -m pip install selenium==4.15.2
python -m pip install pandas==2.1.3
python -m pip install undetected-chromedriver==3.5.4
python -m pip install python-dotenv==1.0.0
python -m pip install beautifulsoup4==4.12.2
python -m pip install lxml==4.9.3
python -m pip install webdriver-manager==4.0.1

echo.
echo ======================================================================
echo Installation complete!
echo You can now run: run_scraper.bat
echo ======================================================================
echo.
pause
