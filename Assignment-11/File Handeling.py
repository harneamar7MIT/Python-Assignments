# File Handling Demonstration

# 1. Writing to a file (creates file if not exists)
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This file is created using Python.\n")
file.close()

# 2. Reading the file
file = open("sample.txt", "r")
content = file.read()
print("File Content after writing:")
print(content)
file.close()

# 3. Appending to the file
file = open("sample.txt", "a")
file.write("This line is added later.\n")
file.close()

# 4. Reading again after appending
file = open("sample.txt", "r")
content = file.read()
print("\nFile Content after appending:")
print(content)
file.close()
