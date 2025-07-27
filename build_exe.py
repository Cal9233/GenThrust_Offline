#!/usr/bin/env python3
"""
Build script to create standalone executable for the Part Lookup application
"""
import os
import sys
import shutil
import subprocess

def main():
    print("Building Offline Part Lookup Application...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Clean previous builds
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Cleaned {folder} directory")
    
    # PyInstaller command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Single executable file
        "--windowed",  # No console window (GUI app)
        "--name", "PartLookup",  # Executable name
        "--icon", "NONE",  # You can add an icon file here if available
        "--add-data", "../assets/AirDataDatabase:AirDataDatabase",  # Include data files
        "offline_part_lookup.py"
    ]
    
    # For Windows, use semicolon instead of colon in add-data
    if sys.platform == "win32":
        cmd[-2] = "--add-data"
        cmd[-1] = "../assets/AirDataDatabase;AirDataDatabase"
    
    print("Running PyInstaller...")
    print(" ".join(cmd))
    
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
    
    if result.returncode == 0:
        print("\nBuild successful!")
        print(f"Executable created in: dist/PartLookup{'.exe' if sys.platform == 'win32' else ''}")
        print("\nTo distribute the application:")
        print("1. Copy the executable from the 'dist' folder")
        print("2. Place it in a folder with the 'AirDataDatabase' directory")
        print("3. The application will automatically find the database files")
    else:
        print("\nBuild failed!")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())