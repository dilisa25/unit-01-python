"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
print("")
print("----Task1-----")
print("")
correct_password = "cat"

password = input("Type password: ")

if password.lower() == correct_password:
    print("correct")


print("")
print("----Task1-----")
print("")
"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
print("")
print("----Task2-----")
print("")

task = input("type something : ")

if task == "":
    print("invaild")
else:
    print("vaild")

  

print("")
print("----Task2-----")
print("")
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
print("")
print("----Task3-----")
print("")

sentence = "I have a Cat and a dog"
new_sentence = sentence.lower().replace ("cat","dog")
print(new_sentence)

print("")
print("----Task3-----")
print("")

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
print("")
print("----Task4-----")
print("")
 
name = input("Name: ")
age = input("Age: ")

my_sentence = f" Hello Im {name} and Im {age} year old. "

print(my_sentence)


print("")
print("----Task4-----")
print("")

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
print("")
print("----Task5-----")
print("")

nmb = 20.1/5.3
txt = f"Result: {nmb:.1f}"
print(txt)
print("")
print("----Task5-----")
print("")