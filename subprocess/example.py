########--- The subprocess module is a versatile tool for running and managing subprocesses in Python --- ######


import subprocess
######  subprocess.run()  #######
# args: The command and its arguments as a list.
# capture_output: If True, captures the standard output and error.
# text: If True, outputs and inputs are strings instead of bytes.
# stdout, stderr: Captured standard output and error (if capture_output is True).

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

# You can run shell commands by passing shell=True, but be cautious as it can pose security risks (e.g., shell injection).

result = subprocess.run('ls -l | grep ".py"', shell=True, capture_output=True, text=True)
print(result.stdout)

# Running a Simple Command 
result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)
print(result.stdout)  # Output: Hello, World!

#### Capturing Output and Errors ####
result = subprocess.run(['ls', 'non_existent_file'], capture_output=True, text=True)
print(f"stdout: {result.stdout}")
print(f"stderr: {result.stderr}")  # stderr: ls: cannot access 'non_existent_file': No such file or directory
print(f"returncode: {result.returncode}")  # returncode: 2


###### Running a Command with Input #####
result = subprocess.run(['python3', '-c', 'print(input())'], input='Hello, World!', capture_output=True, text=True)
print(result.stdout)  # Output: Hello, World!

##### Redirecting Output to a File #####
with open('output.txt', 'w') as f:
    subprocess.run(['echo', 'Hello, File!'], stdout=f)
##################################


######  subprocess.Popen()  ############
# args: The command and its arguments as a list.
# stdout, stderr: Set to subprocess.PIPE to capture output.
# communicate(): Sends data to stdin, reads data from stdout and stderr, and waits for the process to terminate.
# returncode: The return code of the process.

import subprocess
process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()
print(stdout)
if process.returncode != 0:
    print(f"Error: {stderr}")



process = subprocess.Popen(['ping', '-c', '4', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
for line in process.stdout:
    print(line, end='')  # Print each line as it comes
stdout, stderr = process.communicate()
print(f"returncode: {process.returncode}")



# Timeout and Exceptions
import subprocess
try:
    result = subprocess.run(['sleep', '10'], timeout=5)
except subprocess.TimeoutExpired:
    print("Command timed out")


# Using Environment Variables
import subprocess
import os

my_env = os.environ.copy()
my_env['MY_VAR'] = '123'

result = subprocess.run(['printenv', 'MY_VAR'], capture_output=True, text=True, env=my_env)
print(result.stdout)  # Output: 123


# You can use pipes to connect the output of one process to the input of another.
import subprocess

p1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(['grep', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits
output, _ = p2.communicate()

print(output)











  
#####################################
