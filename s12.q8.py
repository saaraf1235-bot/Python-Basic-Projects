class Employee:
    def __init__(self, emp_id, emp_name, department, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        #storing department and salary as tuple
        self.details = (department, salary)
    
    def show_details(self):
        dept, sal = self.details  #unpacking tuple
        print("Employee id is: ",self.emp_id)
        print("Employee name is: ",self.emp_name)
        print("Department is: ",dept)
        print("Salary is: ",sal)


def Database_of_Employee():
    # Dictionary: {emp_id: Employee_object}
    employees = {}
    
    try:
        #adding 3 employees
        employees[101] = Employee(101, "Sayali", "IT", 77000)
        employees[102] = Employee(102, "Shivani", "HR", 70000)
        employees[103] = Employee(103, "Ram", "Finance", 75000)
        
        print("----Database Of Employees----")
        for emp_id, emp_o in employees.items():
            emp_o.show_details()
            
    except Exception as e:
        print("Error in employee database: {}".format(e))

Database_of_Employee()