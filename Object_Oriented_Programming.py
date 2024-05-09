# #Syntax:

# #class <ClassName>
# #    <statement1>
# #    <statement2>
# #
# #    <statementN> 

# class Person:
#     name = 'Skinny'

# Person.name

# details = Person()
# details.name

# # Example of how to define a constructor

# class Person:
#     def __init__(self):
#         print('Constructor Invoked')

# # Instance Attributes
# # class Person:
#     # nationality = 'Ethiopian' / class atribute
#     # def __init__(self): / constructor
#         # self.name = '' / instance attribute
#         # self.age = 0 / instance attribute

# # Setting Attribute Values
# # class Person:
# # name & age parameters passed in constructor
# #   def __init__(self, name, age):
# #       self.name = name
# #       self.age = age

# # Passing Instance Attribute Values in Constructor
# # >>> p1 = Person('Mutemi', 65)
# # >>> p1.name
# # 'Mutemi'
# # >>> p1.age
# # 65

# # Setting Default Values of Instance Attributes
# # class Person
# #    def __init__(self, name="mkuu", age=101)
# #       self.name=name
# #       self.age=age

# # Instance Attribute Default Value
# # Now, you can create an object with default values
# # >>> p1 = Person()
# # >>> p1.name
# # 'Guest'
# # >>> p1.age
# # 65

# # Class Method

# class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

#   def displayInfo(self):
#       print('Person Name:', self.name,'Age:', self.age)

# # Calling a Method
# # Let's call/Invoke the displayInfo method as shown below:
# p1 = Person('Mutemi', 65)
# p1.displayInfo()

# # Deleting atrribute
# std = Person('Mutemi', 65)
# del std.name
# std.name

# # deleting object
# del std
# std.name

# # deleting class
# del Person 
# std = Person('Mutemi', 65)

# Inheritance

# Types in inheritance in Python
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical inheritance 
# 5. Hybrid inheritance

# 1. Single Inheritance 

# Base/Parent class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Parent(Vehicle) class')

# Child class
class Car(Vehicle):
    def Car_info(self):
        print('Inside Child(Car) class')

# Create object of car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.Car_info()

# 2. Multiple Inheritance

# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')

# 3. Multilevel inheritance

# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Car class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside SportsCar class')

# Child class
class SportsCar:
    def sports_car_info(self):
        print('Inside Car class')

# # Create object of SportsCar
# s_car = SportsCar()

# # access Vehicle's and Car info using SportsCar object
# s_car.Vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()

# 4. Hierarchical Inheritance
class Vehicle:
    def info(self):
        print('This is Vehicle')

class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)

class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')

# # 5. Hybrid Inheritance
# # Let's implement heirarchical and multiple inheritance combinations.
# # Creats a Parent class Vehicle and two child classes Car and Truck (hierarchical inheritance)
# # Create another class SportCar that inherits from twon Parent classes named Car and vehicle (Multiple inheritance)

# class Vehicle:
#     def vehicle_info(self):
#         print('Inside Vehicle class')

# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')

# class Truck(Vehicle):
#     def truck_info(self):
#         print('Inside Truck class')

# # Sports Car inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def sports_car_info(self):
#         print("Inside SportsCar class")

# # Create object
# s_car = SportsCar()

# s_car.vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()

# # Python super() function

# class Company:
#     def company_name(self):
#         return 'Google'

# class Employee(Company):
#     def Info(self):
#         # calling the superclass method using the super()function
#         c_name = super().company_name()
#         print("Jessa works at", c_name)

# # Create object of child class
# emp = Employee()
# emp.info()

# # issubclass()

# class Company:
#     def fun1(self):
#         print("Inside parent class.")
# class Employee(Company):
#     def fun2(self):
#         print("Inside child class.")
# class Player:
#     def fun3(self):
#         print("Inside Parent class.")        

# Access modifiers
# 1. Public Access Modifier
# 2. Private Access Modifier
# 3. Protected Access Modifier

# 1. Public Access Modifier

# Example of Public Attributes
class Student:
    schoolName = 'PLP Academy'
    
    def __init__(self, name, age):
        self.name=name
        self.age=age

std = Student('Mkuu', 25)
std.schoolName
std.schoolName
'PLP Academy'
std.name
'Mkuu'
std.age = 28
std.age
28

# Protect Memebers

class Student:
    _schoolName = 'XYZ School'

    def __init__(self, name, age):
        self.name=name
        self._age=age

std = Student('Tembo', 25)
std._name 
'Tembo'
std._name = 'Dax'
std._name 
'Dax'
std._age
25

# Private Members

class Student:
    __schoolName = 'XYZ School'

    def __init__(self, name, age):
        self.__name=name
        self.__salary=age
    def __display(self):
        print('This private method')

std = Student('Bill', 25) 
std._Student__name
"Bill"
std._Student__name = 'Steve'
std._Student__name 
'Steve'
std._Student__display()
'This is private method.'   