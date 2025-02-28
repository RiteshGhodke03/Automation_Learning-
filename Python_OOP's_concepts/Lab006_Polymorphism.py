
#Method overriding
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

# Creating objects
dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Dog barks
cat.make_sound()  # Output: Cat meows
