@echo off
echo ============================================
echo   Installing required Python dependencies...
echo ============================================

:: Upgrade pip first
python -m pip install --upgrade pip

:: Install required packages
pip install requests pyfiglet

echo.
echo ============================================
echo   Installation complete!
echo   You can now run the script with:
echo   python Thumbnail_Stealer.py
echo ============================================

pause