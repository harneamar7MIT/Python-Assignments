# Base Class
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived Class (inherits Person)
class Employee(Person):
    
    def __init__(self, name, age, emp_id, salary):
        # Call constructor of Person
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


# Derived Class (inherits Employee)
class Manager(Employee):
    
    def __init__(self, name, age, emp_id, salary, department):
        # Call constructor of Employee
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


# Creating object of Manager
m1 = Manager("Yuvraj", 21, "E101", 50000, "IT")

# Calling methods
m1.display_person()
m1.display_employee()
m1.display_manager()