#instance variable and class veriable
class Employee:
   
    company_name = "ABC Corporation"  # Class variable

    def __init__(self,emp_name, emp_designation, emp_salary):
        self.emp_name = emp_name  # Instance variable
        self.emp_designation = emp_designation # Instance variable
        self.emp_salary = emp_salary # Instance variable
      
        
        print("Employee Name: ", self.emp_name)
        print("Employee Designation: ", self.emp_designation)
        print("Employee Salary: ", self.emp_salary)
        
        

ravi = Employee("Ravi", "Software Engineer", 50000)
print("Company Name:",ravi.company_name)
print("------------------------------------------")


meera = Employee("Meera","Data Science",750000)
print("Company Name:",meera.company_name)
print("------------------------------------------")