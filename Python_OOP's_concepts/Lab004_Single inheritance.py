class Animal:
    def make_sound(self):
        print("Animal makes sounds")


class Dog(Animal):
    def bark(self):
        print("Dog Bark")

#Creating object

dog = Dog()
dog.make_sound()
dog.bark()