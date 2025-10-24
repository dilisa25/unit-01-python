"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""

"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    #In the case of num2 being zero use except to explain can't divide by zero
    except:
        print("Can't divide by zero")

# Example usage:
divide_numbers(10, 0)

"""
Example 2: Opening Files
"""
def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
    #Can't open read file that doesnt exist
    except FileNotFoundError:
        print("File not found")
 

# Example usage:
read_file("nonexistent.txt")


"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    #In the case of request for item outside of list index
    except IndexError:
        print("List index is out of range")


# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)


"""
Example 4: Dictionaries
"""
def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
    #Use except to explain can't print a value that has not been found in dictitonary 
    except KeyError:
        print("The key has not no been found in dictionary")


# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("File not found.")
    #The else block to executes code if no exceptions were found
    else:
        print("File contents:", contents)
    #Finally block to ensure file was actually opened and read
    finally:
        print("File was read")



# Example usage:
process_file("example.txt")








