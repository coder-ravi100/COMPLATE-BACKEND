#Without Encapsulation
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Ravi",95)
print(s1.marks)

s1.marks = -10 #koi bhi galat value daal diya
print(s1.marks)

# Problem kya hai?

# Koi bhi negative marks daal sakta hai.
# Data unsafe hai.