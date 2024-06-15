# File handling examples in Python

# 1. Writing to a File
# Open a file in write mode ('w'). This will create the file if it does not exist or truncate the file if it exists.
with open('example.txt', 'w') as file:
    file.write('Hello, DevOps!\n')
    file.write('This is a test file.\n')
    print("Data written to 'example.txt'")

# 2. Appending to a File
# Open a file in append mode ('a'). This will create the file if it does not exist and append to the file if it exists.
with open('example.txt', 'a') as file:
    file.write('Appending a new line.\n')
    print("Data appended to 'example.txt'")

# 3. Reading from a File
# Open a file in read mode ('r'). This is the default mode and will raise an error if the file does not exist.
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Content of 'example.txt':")
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")

# 4. Reading File Line by Line
# Using a loop to read each line from the file.
try:
    with open('example.txt', 'r') as file:
        print("Reading 'example.txt' line by line:")
        for line in file:
            print(line, end='')
except FileNotFoundError as e:
    print(f"Error: {e}")

# 5. Reading Specific Number of Characters
# Using the `read` method with a specified number of characters.
try:
    with open('example.txt', 'r') as file:
        content = file.read(5)  # Read the first 5 characters
        print(f"First 5 characters of 'example.txt': {content}")
except FileNotFoundError as e:
    print(f"Error: {e}")

# 6. Using 'with' Statement
# Ensures that the file is properly closed after its suite finishes, even if an exception is raised.
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Content of 'example.txt' using 'with' statement:")
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")

# 7. Writing and Reading Binary Files
# Open a file in binary write mode ('wb') and binary read mode ('rb').
data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)
    print("Binary data written to 'example.bin'")

try:
    with open('example.bin', 'rb') as file:
        binary_content = file.read()
        print("Binary content of 'example.bin':")
        print(binary_content)
except FileNotFoundError as e:
    print(f"Error: {e}")

# 8. Handling Exceptions
# Demonstrating how to handle file-related errors.
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

# 9. Working with File Paths
# Using the `os` module to work with file paths.
import os

file_path = os.path.join(os.getcwd(), 'example.txt')
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Content of '{file_path}':")
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")
