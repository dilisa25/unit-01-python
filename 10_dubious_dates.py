from datetime import datetime
from datetime import date
from datetime import time
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#Prints the current date and time using the datetime module
current_dt = datetime.now()

print(current_dt)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#Prints the current date and time using the datetime module
current_date = datetime.now()

print(current_date)
#Used the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
my_string = current_date.strftime("%m/%d/%Y")

print(my_string)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
#Two random dates as strings  
string1 = "09/11/2008"
string2 = "June 22,2025"
#Used the strptime function to convert the strings into dates
date1 = datetime.strptime(string1, "%m/%d/%Y")
date2 = datetime.strptime(string2, "%B %d,%Y")

print(date1)
print(date2)
#The found the difffrence between the dates
print(date2 - date1)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
# Asks the user for their birthdate then convert the string into a date
your_birthday = input("Whats your birthday?(mm/dd/yyyy): ")
birthday = datetime.strptime(your_birthday, "%m/%d/%Y")
today = datetime.now()
#To get age subract todays year from birthday year 
age = today.year - birthday.year
print("Your age is ",age) 

