
"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
print("------task1-----")
print("")
float_variable = 2.5 
#covert float to interger
converted_interger = int(float_variable) 
#Printed original variable and the converted integer
print(float_variable)
print(converted_interger)
print("")
print("------task1-----")

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
print("------task2-----")
print("")
my_num = 5

if my_num > 0:
    print("its postive")
if my_num < 0 :
    print("its negative")
if my_num == 0:
    print("its zero")
    
print("")
print("------task2-----")
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
print("------task3-----")
print("")
#input for float
input1 = input("give me a float: ")
num1 = float(input1)
print(type(num1))
#input for interger 
input2 = input("give me an interger: ")
num2 = int(input2)
print(type(num2))
#prints out addition, subtraction, multiplication, and division
print(num1*num2)
print(num1+num2)
print(num1/num2)
print(num1-num2)
print("")
print("------task3-----")
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
print("------task4-----")
print("")
#made list of fruits and theri values 
x= {
    'watermelons': 2,
    'pears' : 5 ,
    'apples': 6,
    'oranges': 3  
}
 #printed out the quantity of one of the fruits
print(x['apples'])
print("")
print("------task4-----")
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
print("------task5-----")
print("")
#made string of numbers
string = "3,4,5,6"
#split list apart 
list = string.split(",")
#print the list
print(list)
print("")
print("------task5-----")
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
print("------task6-----")
print("")
s_list =["math","art","english"]
s_string = "|" .join(s_list)
#Print both the original list and both joined strings
print(s_list)
print(s_string)
print("")
print("------task6-----")
