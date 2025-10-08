import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
for x in range (10):
    dice_roll=random.randint(1, 6)
    print("Dice Roll: ") 
    print(dice_roll)
 
    

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
# for x in range (5):
#     generator=random.random-float(1, 5)
#     generator1==random-float(10, 20)

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
for x in range (3):
    my_list=["red", "blue", "green", "yellow", "purple"]
    print(random.choice(my_list)) 

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
