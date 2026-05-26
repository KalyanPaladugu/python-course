#OOP (Object Oriented Programmning)

# Example:ConnectionAbortedError
# 1.Create a design for car --> class
# 2.Create a real product --> object   

# Create a class -> like a blueprint
# class Car: 
#     def __init__(self,make,model,year): #constructor
#         self.make=make  #self is used to refer to the current instance of the class
#         self.model=model
#         self.year=year

#     def display_info(self):
#         print(f"Car: {self.year} {self.make} {self.model}")
# # Create an object
# my_car=Car("Toyota","Camry",2020)
# my_car.display_info()

# Encapsulation: Wrapping data and methods that operate on the data within a single unit (class) and restricting access to some of the object's components. This is done to protect the integrity of the data and prevent unauthorized access.  
# class Bank:
#     def __init__(self):

#         self.__balance=500  # Private attribute
#     def get_balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print(f"Deposited {amount}. New balance: {self.__balance}")

    # def withdraw(self,amount):
    #     if amount>self.__balance:
    #         print("Insufficient funds")
    #     else:
    #         self.__balance-=amount
    #         print(f"Withdrew {amount}. New balance: {self.__balance}")


# c1=Bank()
# # c1.balance=1000   #Directly modifying the balance (not recommended) use encapsulation (__balance)to protect the balance
# c1.__balance=1500  #This will not change the balance because __balance is a private attribute
# print(c1.get_balance())


# Inheritance: A mechanism where a new class (child class) inherits properties and behaviors (attributes and methods) from an existing class (parent class). This promotes code reusability and establishes a natural hierarchical relationship between classes.
# class Employee:
#   def work(self):
#         print("Employee is working")

# class Developer(Employee):  # Developer is a child class of Employee
#     def code(self):
#         print("Developer is coding")

# class Tester(Employee):  # Tester is a child class of Employee
#     def test(self):
#         print("Tester is testing")

# dev=Developer()
# dev.work()  # Inherited method from Employee
# dev.code()  # Developer's own method

# test=Tester()
# test.work()  # Inherited method from Employee
# test.test()  # Tester's own method


#Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.
# class Employee:
#     def work(self):
#         print("Employee is working")
# class Developer(Employee):
#     def work(self):
#         print("Developer is coding")
# class Tester(Employee):
#     def work(self):
#         print("Tester is testing")

# employees=[Developer(),Tester(),Employee()]
# for emp in employees:    emp.work()  # Polymorphic behavior: the same method name 'work' behaves differently based on the object type       


#Abstraction: The concept of hiding the complex implementation details and showing only the necessary features of an object. It allows us to focus on what an object does rather than how it does it.
# from abc import ABC, abstractmethod
from abc import abstractmethod


class ATM:
    @abstractmethod
    def withdraw(self,amount):
        print(f"Withdrawing {amount} from ATM")

class BankATM(ATM):
    def withdraw(self,amount):
        print(f"Withdrawing {amount} from BankATM")

class MobileATM(ATM):
    def withdraw(self,amount):
        print(f"Withdrawing {amount} from MobileATM")
atm1=BankATM()
atm2=MobileATM()
atm1.withdraw(100)  # Output: Withdrawing 100 from BankATM
atm2.withdraw(50)   # Output: Withdrawing 50 from MobileATM

