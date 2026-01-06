# imports
from backend.employee import Employee
class EmployeeManager:
    '''
    Holds a list of employees and implements all business logic:
    adding, deleting, updating, and retrieving employees.
    It does NOT handle user input/output.
    '''
    def __init__(self):
        # Initialize empty list of employees
        self.employees = []

    def add_emp(self, name : str, age : int, salary : int):
        # Adds a new employee object to the list
        self.employees.append(Employee(name, age, salary))
    
    def get_employees(self):
        # Return a copy of the list to prevent external modifications
        return self.employees.copy()
    
    def delete_by_age(self, start : int, end : int):
        '''
        Delete all employees whose age is within [start, end] inclusive.
        Returns a list of deleted employee names for feedback.
        '''
        del_emp_names = []
        # Iterate in reverse to safely remove items while iterating
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if start <= emp.age <= end:
                del_emp_names.append(emp.name)
                self.employees.pop(idx)          # remove employee
        # Reverse the list to preserve original order in feedback
        return del_emp_names[::-1]


    def update_salary(self, name, salary):
        '''
        Updates the salary of the first employee with matching name.
        Returns True if successful, False if employee not found.
        '''
        for emp in self.employees:
            if emp.name == name:
                emp.salary = salary
                return True
        return False

