# Write a Python program to convert the JSON array into a CSV file.

import json
import csv

# Sample JSON data (you can also load from a file)
json_data = '''
[
    {"name": "Himanshu", "age": 20, "city": "Pune"},
    {"name": "Pankaj", "age": 22, "city": "Mumbai"},
    {"name": "Amit", "age": 21, "city": "Delhi"}
]
'''

# Convert JSON string to Python list
data = json.loads(json_data)

# Open CSV file for writing
with open('output.csv', 'w', newline='') as csv_file:
    # Get field names (keys from JSON)
    fieldnames = data[0].keys()
    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write column names
    writer.writerows(data)  # Write data rows

print("CSV file created successfully!")
