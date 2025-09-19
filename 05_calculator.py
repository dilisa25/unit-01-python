# Welcome to the Dilisa's Calculator 9000!

# Enter the first number: 10
# Enter the second number: 5

# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Floor Division
# 6. Exponential
# 7. Remainder

# Enter choice: 3

# Result: 50.0

print("Welcome to the Calculatinator-inator 9000")
print("")
#Ask user for the first and second number 
f_number = float(input("Enter the first number: "))
s_number = float(input("Enter the second number: "))
print("")
#Present user with list of operations 
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
print("")
print("")
#Ask user to enter their choice of operation
choice= input("Enter your choice: ")

#Based on users choice of operation calclate between the first number and second number then print results
if choice == "1":
    results = f_number + s_number
    print(results)
    
elif choice == "2":
    results = f_number - s_number
    print(results)

elif choice == "3":
    results = f_number * s_number
    print(results)

elif choice == "4": 
    #if either or both number imputs are zero
    if s_number == 0:
        print("You cannot calculate with that number")
    else: 
        results = f_number / s_number
        print(results)

elif choice == "5":
    if s_number == 0:
        print("You cannot calculate with that number")
    else: 
        results = f_number // s_number
        print(results)

elif choice == "6":
    results = f_number ** s_number
    print(results)

elif choice == "7":
    if  s_number == 0:
        print("You cannot calculate with that number")
    else: 
        results = f_number % s_number
        print(results)

#If the user inputs an invalid operation tell them it is invalid
else:
    print("Invaild Operation. Please select between 1-7.")