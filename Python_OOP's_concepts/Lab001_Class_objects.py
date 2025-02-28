#Defining a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"car brand: {self.brand}, model:{self.model}")

#creating an object
my_car = Car("Toyota", "Corolla")
my_car.display_info() #calling function


