class Father:
    def father(self):
        print("Father's traits")

class Mother:
    def mother(self):
        print("Mother's traits")

class Child(Father, Mother):
    def child(self):
        print("child has both traits")

#objects

c = Child()
c.mother()
c.father()
c.child()