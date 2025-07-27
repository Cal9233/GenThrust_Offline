#!/usr/bin/env python3
import sys
import os

# First install openpyxl if needed
try:
    import openpyxl
    print("✓ openpyxl is installed")
except ImportError:
    print("Installing openpyxl...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from offline_part_lookup import ExcelReader

# Test reading the Excel file
excel_file = '/var/www/cal.lueshub.com/assets/AirDataDatabase/INVENTORIO ACTUAL GENTHRUST.xlsx'
print(f"\nTesting Excel reader with: {excel_file}")

if os.path.exists(excel_file):
    reader = ExcelReader(excel_file)
    
    print(f"\nFields found: {len(reader.fields)}")
    if reader.fields:
        print("Column headers:")
        for field in reader.fields[:10]:  # Show first 10 fields
            print(f"  - {field['name']}")
        if len(reader.fields) > 10:
            print(f"  ... and {len(reader.fields) - 10} more fields")
    
    print(f"\nRecords found: {len(reader.records)}")
    
    if reader.records:
        print("\nFirst 3 records:")
        for i, record in enumerate(reader.records[:3], 1):
            print(f"\nRecord {i}:")
            # Show non-empty fields
            for key, value in record.items():
                if value and value.strip() and key != '_sheet':
                    print(f"  {key}: {value}")
            if '_sheet' in record:
                print(f"  [From sheet: {record['_sheet']}]")
        
        # Search for part numbers
        print("\n\nSearching for part-related fields...")
        part_fields = []
        for field in reader.fields:
            if any(keyword in field['name'].upper() for keyword in ['PART', 'CODIGO', 'ITEM', 'PN', 'NUMBER']):
                part_fields.append(field['name'])
        
        if part_fields:
            print(f"Found part fields: {part_fields}")
            print("\nSample part numbers:")
            count = 0
            for record in reader.records:
                for field in part_fields:
                    if field in record and record[field].strip():
                        print(f"  - {field}: {record[field]}")
                        count += 1
                        break
                if count >= 5:
                    break
else:
    print(f"Error: Excel file not found at {excel_file}")