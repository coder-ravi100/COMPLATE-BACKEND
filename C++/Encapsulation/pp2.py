#With Encapsulation Using Private Variable
#Python me private variable banane ke liye double underscore use karte hain.

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary,emp_photo):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.__emp_salary =  emp_salary
        self.emp_photo = emp_photo

    def get(self):
        return self.__emp_salary
    def set(self):
        print("Invalid")

e1 = Employee(101,"ravi",25000,"pic_1")
print(e1.get())

# e1.set(15000)
# print(e1.get())
        