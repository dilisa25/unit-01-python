'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
#set interger
my_integer = 5 
#Check if an integer is greater than 10 if so true 
if my_integer > 10:
    print(True)
#False if an integer is not greater than 10
else:
    print(False)

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
# ask user if they are a student and there age
student_status = input("Are you a student? Type Yes or No: ")
age = int(input("Whats your age: "))
# if user over 18 and a student price $10
if age < 18 or student_status == Yes:
    print("The price is $10")
# if not 
else:
    print("The price is $20")



'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
'''
#User iput and list
user_input= input("Enter a fruit name: ")
fruits = ["apple", "orange" "pineapple"]
#if it is, print "Yes, that fruit is in the list
if user_input in fruits:
    print("Yes, that fruit is in the list.")
else:
    print("Fruit not in list")

'''
Exercise 4:Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
#ask user for input 
weight= int(input("What is the weight of your package: "))
zone= input("What zone do you live in A or B : ")

# based on weight and zone print price
if weight <0:
    print("ERROR")
if zone == "A" :
    priceA = weight*5
    print(priceA)
elif zone == "B":
    priceB = weight*7
    print(priceB)



'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
side1 = 3
side2 = 3
side3 = 4

if side1 == side2 == side3:
    print("It's a equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1== side3:
    print("Its a isosocles triangle.")
elif side1 != side2 != side3:
    print("Its a scalene triangle.")
else:
    print("Not a triangle.")
