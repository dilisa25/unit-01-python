"""""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
#set i = to 1
i=1 
#created a while statement that added 1 to i until it less than 11
while i < 11:
    print(i)
    i +=1 
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print("")
a=10 
#created a while statement that subtracted 1 from a until it reahced 1
while a > 0:
    print(a)
    a -=1 
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
#ask user for input 
num = int(input("Give me a number: "))
#Set result as 1 as a place holder
result = 1
#Made a loop so that num keeps mutipling by result until as long as the number is less than 0 
while num > 0:
    #Made the result mutiple by the num to give the new result using factorial math 
    result = num * result
    # Decrease number by 1 to get the next number in the factorial seqeunce 
    num -= 1 

print(result)
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
#set password then asked user to guess my password 
password = "cat"
pswd = input("Guess my password!")
# if user inputs incorrect password while statment keeps asking until they get it right
while password != pswd:
    print("Try again!")
    pswd = input("Guess my password!")
# if user gets right tell them you got it correct
else:
    print("You got it correct!")
    




"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""