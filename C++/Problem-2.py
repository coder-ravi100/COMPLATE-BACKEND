#Problem 2: Student System
class Student:
    def __init__(self,name, marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total_marks(self):
        self.student_marks = self.marks1 + self.marks2 + self.marks3
        
    def avg(self):
        self.student_avg = self.student_marks / 3

    def result(self):
        if self.student_marks >= 80:
            self.result = "Pass"
        else:
            self.result = "Fail"


    def display(self):
        print("Student Name :",self.name)
        print("Student Total Marks :",self.student_marks)
        print("Student Average :",self.student_avg)
        print("Student Result :",self.result)

        
s1 = Student("Ravi",50,60,50)
s1.total_marks()
s1.avg()
s1.result()
s1.display()


