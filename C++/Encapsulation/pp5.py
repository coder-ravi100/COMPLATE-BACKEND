#Access Modifier ------>Encapsulation
## public

class Person:
    ## constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def display(self):
        print("Person Name is :{self.name} and age is {self.age}")

p1 = Person("Krishana",27)
p1.display()
