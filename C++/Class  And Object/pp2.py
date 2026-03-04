#init and self method   __init__(self)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Name: ",self.name)
        print("Age: ",self.age)

ravi = person("Ravi", 20)
shyaam = person("Shyaam", 21)
