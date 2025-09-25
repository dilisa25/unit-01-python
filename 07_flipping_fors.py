"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#set variable equal to my name 
name= "Dilisa"
#Created for loop to print each character in my name 
for char in name:
    print(char)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#Created a list of numbers 
num = [8 , 2 ]
#Set result as 0 as a place holder
result = 0 
#Created a for loop to calculate the sum of the numbers in the list 
for x in num:
    result += x
    print(result)


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#Created sentence then changed it into the list using the split function
sentence = ("My name is Dilisa") 
my_list= sentence.split(" ")
#Created a for loop to print the length of each word in the sentence that was chnged into in list 
for x in my_list:
    print(len(x))
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
# I noticed that when I run it intially that it only prints about the name of the signs and not the value 
#created a dictionary
signs = {
    "love" : 2, 
    "peace": 3,
    "hapiness":4,
    "sadness":101
    }
# Created a for lopp that iterates through the dictionary and prints the result
for x in signs:
    print("Key:")
    print(x)
    print("Value:")
    print(signs[x])