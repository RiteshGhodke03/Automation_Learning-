#Abstraction is used to hide implementation details and only show the essential features.

from abc import ABC, abstractmethod  # Importing ABC module

class Vehicle(ABC):  # Abstract class

    @abstractmethod
    def start(self):  # Abstract method
        pass

class Car(Vehicle):  # Concrete class
    def start(self):
        print("Car is starting with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a self-start button")

# Creating objects
car = Car()
bike = Bike()

car.start()  # Output: Car is starting with a key
bike.start()  # Output: Bike is starting with a self-start button
