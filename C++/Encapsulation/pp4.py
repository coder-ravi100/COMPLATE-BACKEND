#Access Modifier ------>Encapsulation
## Protected

class Person:
    ## constructor
    def __init__(self, name, age):
        self._name = name # single underscore use
        self._age = age

class Student(Person):
    
    def __init__(self,name,age):
        super().__init__(name,age)

    def display(self):
        print(f"The Person Name is {self._name} and the age is {self._age}")

s1 = Student("Ravi",26)
s1.display()
