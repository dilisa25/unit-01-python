"""
Task 1: Greeting
Write a function that takes a name and says hi to them.
"""
def my_function(name): 
    #Prints a hello to with the name given
    print("Hello " + name)

my_function("Dilisa") #print the function using my name

"""
Task 2: Square of a Number
Take a number and give me its square.
"""
def square_num(a): 
    # Multiply the number by itself to get the square
    return a * a

print(square_num(2)) 


"""
Task 3: Even or Odd
Check if a number is even or odd.
"""
def even_or_odd(num): 
    # If it divides by 2 cleanly, it's even. Otherwise, odd.
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2))  

"""
Task 4: Area of a Rectangle
Find the area using length and width.
"""
def areaofrect(l , w): 
    # Mutiple length and width
    return l * w

print(areaofrect(2,8)) 

"""
Task 5: Celsius to Fahrenheit
Convert a temp from C to F.
"""
def convert(celius): 
    # Convert to Fahrenheit 
    return celius * 2 + 30

print(convert(10)) 
"""
Task 6: Average of Numbers
Take a list of numbers and find the average.
"""
def average(numbers): 
    #Add numbers up and divide by how many numbers there are
    return sum(numbers)/len(numbers)

print(average([1,2,4]))  

"""
Task 7: Total Calculator
Figure out total price with optional discount.
"""
def total_calculator(price,quanity,discounts=0.0): 
    # Multiply price by quantity for subtotal
    subtotal = price * quanity 
    # Subtract discount if there is one
    return subtotal- (subtotal * discounts)

print(total_calculator(3,4))
