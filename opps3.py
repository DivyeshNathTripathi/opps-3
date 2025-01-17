# -*- coding: utf-8 -*-
"""opps3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12CSOhgbfhS3piCAFeMQfKG3etv7aVK7r

Q1: Create a Vehicle class with an __init__ method having instance variables as name_of_vehicle, max_speed, and average_of_vehicle.

**Amswer:**
"""

class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

# Example
vehicle = Vehicle("Bike", 120, 50)
print(f"Vehicle Name: {vehicle.name_of_vehicle}, Max Speed: {vehicle.max_speed}, Average: {vehicle.average_of_vehicle}")

"""Q2: Create a child class Car from the Vehicle class, which will inherit the Vehicle class. Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

**Answer:**
"""

class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity}."

# Example
car = Car("Sedan", 180, 15)
print(car.seating_capacity(5))

"""Q3: What is multiple inheritance? Write a Python code to demonstrate multiple inheritance.

**Answer:**
Multiple inheritance is a feature of OOP where a class can inherit from more than one base class. This allows the derived class to access attributes and methods from all the parent classes.

**Example:**
"""

class Engine:
    def engine_type(self):
        return "This vehicle has a petrol engine."

class Transmission:
    def transmission_type(self):
        return "This vehicle has a manual transmission."

class Car(Vehicle, Engine, Transmission):
    pass

# Example
car = Car("SUV", 200, 12)
print(car.engine_type())
print(car.transmission_type())

"""Q4: What are getters and setters in Python? Create a class with a getter and setter method.

**Answer:**
Getters and setters are used to access and modify private instance variables in Python.

**Example:**
"""

class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, name):
        self.__name = name

# Example
student = Student("Alice", 20)
print(student.name)  # Using the getter
student.name = "Bob"  # Using the setter
print(student.name)

"""Q5: What is method overriding in Python? Write a Python code to demonstrate method overriding.

**Answer:**
Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. The overridden method in the child class has the same name, parameters, and return type as the one in the parent class.

**Example:**
"""

class Vehicle:
    def describe(self):
        return "This is a generic vehicle."

class Car(Vehicle):
    def describe(self):
        return "This is a car."

# Example
vehicle = Vehicle()
car = Car()
print(vehicle.describe())  # Output: This is a generic vehicle.
print(car.describe())      # Output: This is a car.