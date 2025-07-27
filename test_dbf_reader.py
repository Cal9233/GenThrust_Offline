#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from offline_part_lookup import DBFReader

# Test reading a DBF file
test_file = '/var/www/cal.lueshub.com/assets/AirDataDatabase/ALTPART.DBF'
print(f"Testing DBF reader with: {test_file}")

reader = DBFReader(test_file)

print(f"\nFields found: {len(reader.fields)}")
for field in reader.fields:
    print(f"  - {field['name']} (Type: {field['type']}, Length: {field['length']})")

print(f"\nRecords found: {len(reader.records)}")
if reader.records:
    print("\nFirst record:")
    for key, value in reader.records[0].items():
        if value.strip():
            print(f"  {key}: {value}")

# Test with a larger file
test_file2 = '/var/www/cal.lueshub.com/assets/AirDataDatabase/INVENT.DBF'
print(f"\n\nTesting with larger file: {test_file2}")
reader2 = DBFReader(test_file2)
print(f"Fields: {len(reader2.fields)}, Records: {len(reader2.records)}")

# Show some sample part numbers if found
part_fields = [f['name'] for f in reader2.fields if 'PART' in f['name'].upper()]
if part_fields and reader2.records:
    print(f"\nSample part numbers from field '{part_fields[0]}':")
    count = 0
    for record in reader2.records[:100]:
        if part_fields[0] in record and record[part_fields[0]].strip():
            print(f"  - {record[part_fields[0]]}")
            count += 1
            if count >= 5:
                break