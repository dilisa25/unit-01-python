"""
Task 1: Greeting
Write a function that takes a name and says hi to them.
"""
def my_function(name): 
    """
    Prints a greeting using the given name.
    """
    print("Hello " + name)

my_function("Dilisa")  # Print the function using my name

"""
Task 2: Square of a Number
Take a number and give me its square.
"""
def square_num(a): 
    """
    Returns the square of the input number.
    """
    return a * a

print(square_num(2)) 

"""
Task 3: Even or Odd
Check if a number is even or odd.
"""
def even_or_odd(num): 
    """
    Returns 'Even' if the number is divisible by 2, otherwise 'Odd'.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2))  

"""
Task 4: Area of a Rectangle
Find the area using length and width.
"""
def areaofrect(l, w): 
    """
    Returns the area of a rectangle given length and width.
    """
    return l * w

print(areaofrect(2, 8)) 

"""
Task 5: Celsius to Fahrenheit
Convert a temp from C to F.
"""
def convert(celsius): 
    """
    Converts Celsius to Fahrenheit (approximation).
    """
    return celsius * 2 + 30

print(convert(10)) 

"""
Task 6: Average of Numbers
Take a list of numbers and find the average.
"""
def average(numbers): 
    """
    Returns the average of a list of numbers.
    """
    return sum(numbers) / len(numbers)

print(average([1, 2, 4]))  

"""
Task 7: Total Calculator
Figure out total price with optional discount.
"""
def total_calculator(price, quantity, discounts=0.0): 
    """
    Calculates total price by multiplying price by quantity 
    and subtracting any discounts.
    """
    subtotal = price * quantity 
    return subtotal - (subtotal * discounts)

print(total_calculator(3, 4))