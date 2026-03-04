#Employee salary calculation
class Employee:
    def  __init__(self,emp_id, emp_name, emp_designation, basic_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_designation = emp_designation
        self.basic_salary = basic_salary

        
    def display(self):
            print("Employee ID:", self.emp_id)
            print("Employee Name:", self.emp_name)
            print("Employee Designation:", self.emp_designation)
            print("Net Salary:", self.basic_salary)
            print("-----------------------------------------------")

e1 = Employee(101, "Ravi", "Backend Developer", 50000*12)
e1.display()

e2 = Employee(102, "Priya", "Frontend Developer", 45000*12)
e2.display()

e3 = Employee(103, "Amit", "Full Stack Developer", 60000*12)
e3.display()

e4 = Employee(104, "Sneha", "Data Scientist", 55000*12)
e4.display()

e5 = Employee(105, "Rahul", "DevOps Engineer", 48000*12)
e5.display()