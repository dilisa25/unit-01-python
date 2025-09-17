"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print("")
print("----Task1-----")
print("")
#made a list of animals and printed the list
animals = ["cat", "dog", "hamster", "bunny"]
print(animals)

print("")
print("----Task1-----")
print("")
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.


"""
print("")
print("----Task2-----")
print("")
#added "tiger " as a element
animals.append("tiger")
#printed new list
print(animals)

print("")
print("----Task2-----")
print("")
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print("")
print("----Task3-----")
print("")
# removed element "hamster" from list
animals.remove ("hamster")
#printed new list
print(animals)
print("")
print("----Task3-----")
print("")
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print("")
print("----Task4-----")
print("")
#replace index 1 with eagle
animals[1] = "eagle"
#print new list
print(animals)
print("")
print("----Task4-----")
print("")
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
print("")
print("----Task5-----")
print("")
#added mutiple elements
animals.append("raven")
animals.append("snake")
animals.append("wolf")
animals.append("duck")
#printed list
print(animals)
print("")
print("----Task5-----")
print("")
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print("")
print("----Task6-----")
print("")
#Deletes an element at a specific index
del animals[0]
#Printed the updated list
print(animals)
print
print("")
print("----Task6-----")
print("")
"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print("")
print("----Task7-----")
print("")
#created varariable of first 2 items, then print
print(animals[0:2])

print("")
print("----Task7-----")
print("")
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
print("")
print("----Task8-----")
print("")
# Created a new list
animals2 = ["mouse", "horse", "zebra"]
# Added new list to intial list, then print it
final_list = animals + animals2
print(final_list)
print("")
print("----Task8-----")
print("")