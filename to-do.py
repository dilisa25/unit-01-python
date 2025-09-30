todolist=[]
#create while loop so code runs forever 

while True:

    print("Your To-Do List:")
    print()
    
    #ask user if they would like to add or delete  
    add_del= input("Would you like to add or delete?")
    
    #if they pick add, add item to list using append 
    if add_del == "add":
        print()
        add = input("What would you like to add?: ")
        print()
        todolist.append(add)
        print(add)
        print()
        print("Your current to-do list " )
        print()
    #if they pick delete, delete item to list using del  
    if add_del == "delete":
        print()
        delete = int(input("What # task would like to remove?: "))
        print()
        #User doesnt know computer starts counting at 1 so [delete - 1]
        del todolist [delete - 1]
        print("Your current to-do list " )
        print()