
"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
float_variable = 2.5 
#covert float to interger
converted_interger = int(float_variable) 
#Printed original variable and the converted integer
print(float_variable)
print(converted_interger)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
number = 5 
 



"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
#assign interger and float its value 
interger = 3
float = 3.5
#prints out addition, subtraction, multiplication, and division
print(interger*float)
print(interger+float)
print(interger/float)
print(interger-float)

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#made list of fruits and theri values 
x= {
    'watermelons': 2,
    'pears' : 5 ,
    'apples': 6,
    'oranges': 3  
}
 #printed out the quantity of one of the fruits
print(x['apples'])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
#made string of numbers
string = "3,4,5,6"
#split list apart 
list = string.split(",")
#print the list
print(list)

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
s_list =["math","art","english"]
s_string = "|" .join(s_list)
#Print both the original list and both joined strings
print(s_list)
print(s_string)
