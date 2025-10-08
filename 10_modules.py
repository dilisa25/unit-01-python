import os 
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print()
print()
#Created code that prints the current folder using the os module
fldr= os.getcwd()
print(fldr)
print()
print()
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print()
print()
#After creating the test folder, print a list of all files and directories in the current directory
dlist = os.listdir()
print(dlist )
print()
print()
"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print()
#After creating data folder checks if a directory called "data" exists in the current us if statement 
if os.path.exists("data"):
    print("Directory already exists.")
#If path doesnt exist create directory 
else:
    os.mkdir("data")
print()
print()
"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print()
print()
#checks if a file called "config.txt" exists in the current directory and print 
if os.path.isfile("config.txt"):
    print(os.path.abspath("config.txt"))
#If it doesn't exist, print "File not found."
else:
    print("File not found.")
print()
print()

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
#Printed the Python version Im currently using 
print("My current python version is:")
print(sys.version)

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
#made variable for the platform my Python interpreter is running on
platform = sys.platform

#Print output of the correct platform using if statement 
if platform == 'linux':
    print("Linux")
elif platform == 'win32':
    print("Windows")
elif  platform == 'darwin':
    print("MacOS")
else:
    print("Not applicable")
