#Create Employee Class And And Display Employee Salary And Attendance 
class Employee:
    def __init__(self, name , salary , task):
        self.name = name
        self.salary = salary
        self.task = task
        
    def attendance_calculate(self):
       self.attendance = 20
       self.total_days = 30
       
    
    def salary_calculate(self):
        per_day = 500
        self.final_salary = self.attendance * per_day
    
    def display(self):
        print("Employee Name : ",self.name)
        print("Employee Task :",self.task)
        print("Employee Attendance :",self.attendance)  
        print("Salary :",self.final_salary)
    
e1 = Employee("Ravi",25000,"Create Login Page")

e1.attendance_calculate()
e1.salary_calculate()
e1.display()