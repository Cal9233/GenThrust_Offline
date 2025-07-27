# GenThrust_Offline - Offline Part Lookup Application

A standalone desktop application for searching aircraft parts by part number from DBF database files. Works completely offline without internet connection.

## Features

- **Fast Search**: Search through multiple DBF database files instantly
- **Partial Matching**: Find parts with partial part number matches
- **Detailed Results**: View all available information for matching parts
- **Simple Interface**: Easy-to-use GUI with search and clear buttons
- **No Installation**: Runs as a single executable file

## System Requirements

- Windows 7 or later (64-bit recommended)
- No internet connection required
- No Python installation required (for the .exe version)

## Installation

1. Copy the `PartLookup.exe` file to your computer
2. Create a folder structure like this:
   ```
   PartLookup/
   ├── PartLookup.exe
   └── AirDataDatabase/
       ├── INVENT.DBF
       ├── POITEM.DBF
       ├── BUYQUOTE.DBF
       ├── ALTPART.DBF
       └── (other DBF files)
   ```
3. Ensure all DBF files are in the `AirDataDatabase` folder

## Usage

1. Double-click `PartLookup.exe` to start the application
2. Enter a part number in the search box
3. Press Enter or click the "Search" button
4. View matching results in the text area
5. Click "Clear" to reset and search for another part

## Search Tips

- The search is case-insensitive (e.g., "abc123" will find "ABC123")
- Partial matches are supported (e.g., searching "123" will find "ABC123")
- The application searches through multiple database files automatically
- Results show all available fields for each matching record

## Troubleshooting

**Application won't start:**
- Ensure the `AirDataDatabase` folder is in the same directory as the .exe
- Try running as administrator
- Check Windows Defender or antivirus isn't blocking the application

**No results found:**
- Verify the DBF files are present in the `AirDataDatabase` folder
- Try searching with a shorter part number
- Check if the part number exists in your database

**Error loading data:**
- Ensure DBF files are not corrupted
- Check that you have read permissions for the DBF files
- The application folder might need to be on a local drive (not network)

## Building from Source

If you need to rebuild the application:

1. Install Python 3.7 or later
2. Install PyInstaller: `pip install pyinstaller`
3. Run: `pyinstaller --onefile --windowed --name PartLookup offline_part_lookup.py`
4. The executable will be in the `dist` folder

## Data Files

The application reads from these DBF files (in order of priority):
- INVENT.DBF - Main inventory database
- POITEM.DBF - Purchase order items
- BUYQUOTE.DBF - Buy quotes
- ALTPART.DBF - Alternative part numbers
- KIT.DBF - Kit information

## License

For internal use only.
