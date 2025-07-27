@echo off
echo Building Offline Part Lookup Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Install PyInstaller if needed
echo Checking for PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Build the executable
echo.
echo Building executable...
pyinstaller --onefile --windowed --name PartLookup --distpath ./dist offline_part_lookup.py

if exist dist\PartLookup.exe (
    echo.
    echo BUILD SUCCESSFUL!
    echo.
    echo Executable created: dist\PartLookup.exe
    echo.
    echo To use the application:
    echo 1. Copy PartLookup.exe to the destination computer
    echo 2. Place the AirDataDatabase folder in the same directory as the exe
    echo 3. Double-click PartLookup.exe to run
    echo.
) else (
    echo.
    echo BUILD FAILED!
    echo Check the error messages above.
    echo.
)

pause