#empty diction
contacts = {}

while True:
    print("Contact Book Menu ")
    print()
    print()
    print("1. Add Contact")
    print()
    print("2. Delete Contact")
    print()
    print("3. List Contacts")
    print()
    print("4. Exit")
    
    
    choice = input("Enter yout choice(1-4) ")
    if choice == "1":
        name = input("Enter Contact Name: ")
        number = input("Enter Phone Number: ")
        contacts[name] = number
        print("Contact added successfully")
        print()
    elif choice == "2":
        name = input("Enter Contact Name: ")
        if name in contacts:
        del contacts[name]
        print("Contact removed successfully")
        print()
        
    elif choice == "3":
        print("Contacts:")
        for x in contacts:
            print(x,":",contacts[x])
            print()
    elif choice == "4":
        break
    else:
        print("Not Appilcale") 


        
            

