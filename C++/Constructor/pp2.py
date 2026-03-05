#paramiterize Constructor
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Ravi",25000)
print(e1.__dict__) #key value ki pair main value show hoga

print(e1.name) #particular Value print hooga
print(e1.salary)