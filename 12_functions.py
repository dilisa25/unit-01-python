"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
def my_function(name): 
    print("Hello " + name)

my_function("Dilisa")
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square_num(a): 
    return a * a
print(square_num(2))


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def even_or_odd(num): 
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(2))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def areaofrect(l , w): 
    return l * w
print(areaofrect(2,8))


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def convert(celius): 
    return celius * 2 + 30
print(convert(10))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
def average(numbers): 
    return sum(numbers)/len(numbers)
print(average([1,2,4]))

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
def total_calculator(price,quanity,discounts=0.0): 
    subtotal = price * quanity 
    return subtotal- (subtotal * discounts)
  

print(total_calculator(3,4))



