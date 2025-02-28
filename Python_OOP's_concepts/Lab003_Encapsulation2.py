class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p = Person(29)
print(p.get_age())

