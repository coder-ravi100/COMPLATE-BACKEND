#access modifier ---->Encapsulation
##private
class Person:
    # constructor
    def __init__(self,name, age):
        self.__name=name
        self.__age=age

    def display(self):
        print(f"The Person name is {self.__name} and age is {self.__age}")

p1 = Person("Meera",26)
# print(p1.__name)
p1.display()
# dir(Person)
