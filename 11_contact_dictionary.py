
# Created an empty dictionary to store the contacts
contacts = {}

# Used While loop 
while True:
    # Display the Conatct Book Menu 
    print("Contact Book Menu")
    print()
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")
    
    # Ask the user for choice on menu 
    choice = input("Enter your choice (1-4): ")

    # If they pick 1 add a new contact 
    if choice == "1":
        name = input("Enter Contact Name: ")
        number = input("Enter Phone Number: ")
        #Made  sure a user only enters numbers not letters and made sure the phone number is only 10 digits
        if not number.isdigit or len(number) > 10:
            print("Input has to be numbers and cant be more than 10 digits") #Make sure  
        else:
            contacts[name] = number  # Add the contact to the dictionary
            print("Contact added successfully!")
            print()

    # If they pick 2 delete existing contact 
    elif choice == "2":
        name = input("Enter Contact Name: ")
        if name in contacts:
            del contacts[name]  # Remove contact from dictionary
            print("Contact removed successfully!")
        else:
            print("Contact not found.")  # if name doesn't exist
        print()

    # If they pick 3 list all contacts
    elif choice == "3":
        print("Contacts:")
        for x in contacts:
            print(x, ":", contacts[x])
        print()

    # If they pick 4 exit the program
    elif choice == "4":
        print("Exiting Contact Book... Goodbye!")
        break

    # Anything else is an invalid input 
    else:
        print("Not Applicable. Please choose between 1-4.")
        print()



        
            

