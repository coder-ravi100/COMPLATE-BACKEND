#Problem 2: Student System
class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total_marks(self):
        self.total = self.marks1 + self.marks2 + self.marks3

    def average(self):
        self.avg = self.total / 3

    def result(self):
        if self.avg >= 40:
            self.result_status = "Pass"
        else:
            self.result_status = "Fail"

    def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.total)
        print("Average:", self.avg)
        print("Result:", self.result_status)


s1 = Student("Ravi", 50, 60, 50)

s1.total_marks()
s1.average()
s1.result()
s1.display()


