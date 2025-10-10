import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
#Use for loop so it simulates rolling a six-sided die 10 times
for x in range (10):
    #Use random.rant to generate a random number from 1-6 and print 
    dice_roll=random.randint(1, 6)
    print("Dice Roll: ") 
    print(dice_roll)
 
    

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
#Use random.uniform to generates 5 random floating-point numbers between 0 and 1
random1_5 = [random.uniform(0.0, 1.0) for x in range (5)]
#Use random.uniform to generates 5 random floating-point numbers between 10 and 20
random10_20 = [random.uniform(10.0, 20.0) for x in range (5)]
#Then I printed both sets of numbers
print(random1_5)
print(random10_20)

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
#Use for loop to ensure that program prints a color 3 times 
for x in range (3):
    my_list = ["red", "blue", "green", "yellow", "purple"]
    #use random.choice so it randomly selects and prints 3 colors from my list 
    print(random.choice(my_list)) 

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
#Create list from 1 to 10
my_list = list(range(1, 11))
#Used random.shuffle to shuffle that list, then printed it 
random.shuffle(my_list)
print(my_list)



