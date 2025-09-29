"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#Created for loop to print numbers from 1 to 10  usinf range from (1, 11)  
for x in range(1, 11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#Created for loop to count by 10s from 900 to 1000 using range (0, 1001, 10) 
for x in range(0, 1001, 10):
    print(x)
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#Created for loop that counts form 1-100 by 9 using range (1, 101, 9)
for x in range(1, 101, 9):
    print(x)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
# Placeholder for the total sum, starting at 0
sum = 0 
# Created a for loop that counts fro 1-10s using the range (1, 11)
for x in range(1, 11):
    # Add the x to the sum each time to calculate the sum of all numbers from 1 to 10
    sum += x
# Print the final sum after the loop ends
print(sum)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
The ouput of this code is 5 rows of asterisks with the number of asterisks increasing by one each row.

"""
#Explain the iterative process that this code executes to get that output

rows = 5
#This for loop runs 5 times because the range rows which equals 5
for i in range(rows):
    #This inner for loop prints a number of * based on the row number by adding 1 each loop, so the first row prints 1 *, the second row prints 2 *, and so on.
    for j in range(i + 1):
        print('*', end=' ')
    print() #This ensures the asterisks actually print on the following row