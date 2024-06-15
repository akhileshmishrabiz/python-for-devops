

# Getting Current Working Directory: Uses os.getcwd() to get the current directory.
# Changing the Current Working Directory: Changes the working directory using os.chdir().
# Listing Files in a Directory: Lists files in the current directory using os.listdir().
# Making a New Directory: Creates a new directory using os.mkdir().
# Removing a Directory: Removes a directory using os.rmdir().
# Renaming a File or Directory: Renames a file using os.rename().
# Removing a File: Removes a file using os.remove().
# Working with Environment Variables: Gets and sets environment variables using os.getenv() and os.environ.
# Running System Commands: Runs a system command using os.system().
# File Path Operations: Performs various file path operations such as getting the absolute path, checking existence, checking if it's a file or directory, getting the file size, splitting a path, and joining paths using os.path.
# Traversing a Directory Tree: Walks through a directory tree using os.walk().


import os

# 1. Getting Current Working Directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# 2. Changing the Current Working Directory
new_dir = '/tmp'  # Change this path as per your system
try:
    os.chdir(new_dir)
    print(f"Changed Working Directory to: {new_dir}")
except FileNotFoundError as e:
    print(f"Error: {e}")

# 3. Listing Files in a Directory
files = os.listdir('.')
print(f"Files in {os.getcwd()}: {files}")

# 4. Making a New Directory
new_directory_name = 'new_dir'
try:
    os.mkdir(new_directory_name)
    print(f"Directory '{new_directory_name}' created")
except FileExistsError as e:
    print(f"Error: {e}")

# 5. Removing a Directory
try:
    os.rmdir(new_directory_name)
    print(f"Directory '{new_directory_name}' removed")
except FileNotFoundError as e:
    print(f"Error: {e}")

# 6. Renaming a File or Directory
old_name = 'example.txt'
new_name = 'example_renamed.txt'
try:
    with open(old_name, 'w') as f:
        f.write('This is a test file.')
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'")
except FileNotFoundError as e:
    print(f"Error: {e}")

# 7. Removing a File
try:
    os.remove(new_name)
    print(f"File '{new_name}' removed")
except FileNotFoundError as e:
    print(f"Error: {e}")

# 8. Working with Environment Variables
# Get an environment variable
path = os.getenv('PATH')
print(f"PATH environment variable: {path}")

# Set an environment variable
os.environ['MY_VAR'] = '123'
print(f"MY_VAR set to: {os.getenv('MY_VAR')}")

# 9. Running System Commands
exit_code = os.system('echo Hello, World!')
print(f"Command executed with exit code: {exit_code}")

# 10. File Path Operations
# Getting the absolute path
rel_path = 'example.txt'
abs_path = os.path.abspath(rel_path)
print(f"Absolute path of '{rel_path}': {abs_path}")

# Checking if a path exists
path_exists = os.path.exists(abs_path)
print(f"Does the path exist? {path_exists}")

# Checking if it's a file or directory
is_file = os.path.isfile(abs_path)
is_dir = os.path.isdir(abs_path)
print(f"Is it a file? {is_file}")
print(f"Is it a directory? {is_dir}")

# Getting file size
if is_file:
    file_size = os.path.getsize(abs_path)
    print(f"Size of '{abs_path}': {file_size} bytes")

# Splitting a path
dir_name, base_name = os.path.split(abs_path)
print(f"Directory: {dir_name}, Base Name: {base_name}")

# Joining paths
joined_path = os.path.join(dir_name, base_name)
print(f"Joined path: {joined_path}")

# 11. Traversing a Directory Tree
print("Walking through the directory tree:")
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"Found directory: {dirpath}")
    for dirname in dirnames:
        print(f"  Directory: {dirname}")
    for filename in filenames:
        print(f"  File: {filename}")
