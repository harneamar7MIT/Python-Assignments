# Write a Python program to count the total number of rows in a CSV file.

import csv

def count_rows_in_csv(filename):
    try:
        # Open the CSV file in read mode
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            row_count = 0
            
            # Count rows
            for row in reader:
                row_count += 1
            
            print("Total number of rows in the CSV file:", row_count)

    except FileNotFoundError:
        print("Error: File not found.")
    
    except PermissionError:
        print("Error: Permission denied.")
    
    except UnicodeDecodeError:
        print("Error: Encoding issue.")
    
    except IsADirectoryError:
        print("Error: Given path is a directory.")
    
    except csv.Error:
        print("Error: CSV file format issue.")

# Main execution
filename = input("Enter CSV file name: ")
count_rows_in_csv(filename)
