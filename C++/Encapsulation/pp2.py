#With Encapsulation Using Private Variable
#Python me private variable banane ke liye double underscore use karte hain.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks #private Variable

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,value):
        
        if value >= 0:
            self.__marks = value

        else:
            print("Bhai Yaha Lock Laga Hai Yaha Teri Dal Nahi Galegi 🤣")

s1 = Student("Ravi",85)
print(s1.get_marks())

s1.set_marks(-50) #invalid
print(s1.get_marks())
    
#output : 
# 85
# Invalid marks
# 85