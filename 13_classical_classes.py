
"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
# Defined a class called Person with attributes name and age.
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
    #function within the class to introduce the person with their name and age.
   def hola(self):
       print(f"Hi my name is  {self.name} and I'm {self.age} years old" )
#Created a new object using this new class, and called the method I created.
dilisa = Person("Dilisa", 17)
dilisa.hola()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
#created a base class Animal with a empty method called speak. 
class Animal:
    def speak(self):
        pass
#created two subclasses, Dog and Cat, each with their own speak method. 
class Dog(Animal):
    def speak(self):
        print("bark")
class Cat(Animal):
    def speak(self):
        print("meow")  

#created objects using these subclasses and call the speak method.
my_dog = Dog()
my_cat = Cat()

my_dog.speak()
my_cat.speak()

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
#created a class BankAccount with attributes balance and owner. 
class BankAccount:
    
    def __init__(self, owner, balance):
       self.owner = owner
       self.balance = balance
    #Methods for depositing and withdrawing money, which modify the balance attribute.
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"New balance {self.balance}")
        else:
            print("Cant deposit 0.")
    def withdrawl(self,amount):
        if amount > 0:
            self.balance -= amount
            print(f"New balance {self.balance}")
            print
        else:
            print("Cant withdraw 0.")

#Test the methods 
the_account = BankAccount("Val",1000)

the_account.deposit(500)
the_account.withdrawl(25)


