"""
Employee System
Author: Mostafa Osama
Date: 2025-12-17
Description:
    A simple Python program to manage employees with OOP.
    Features: Add, list, delete by age, update salary.
"""
class Employee:
    '''
    Holds employee data
    This class is only a data container
    '''
    def __init__(self, name : str, age : int, salary : int):
        # Assign attributes directly
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        # Friendly string representation for printing to users
        return f'Employee {self.name} has age {self.age} and salary {self.salary}'
    
    def __repr__(self):
        # Developer-friendly representation for debugging
        return f'{self.name} -> age : {self.age}, salary : {self.salary}'
    
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


class Frontend:
    '''
    Handles all user input/output.
    Runs the main loop and calls EmployeeManager for operations.
    '''
    def __init__(self):
        # Initialize the manager object
        self.manager = EmployeeManager()

    def start_menu(self):
        # Prints the main menu
        choices = ['Enter your choice:', '\t1) Add new employee', '\t2) Print all employees',
                        '\t3) Delete by age', '\t4) Update Salary by name', '\t5) End the program']
        print('\n'.join(choices))
    
    def get_choice(self, start : int, end : int):
        # Get choice from user input
        self.choice = int(input())

        if start <= self.choice <= end :
            return self.choice
        print('Invalid input!!\nTry again')
        return        # Returns None if invalid
        
    def get_emp_data(self):
        # Collect employee information from user input
        name = input('Enter employee name : ')
        age = int(input('Enter employee age :'))
        salary = int(input('Enter employee salary :'))
        return name, age, salary

    def run(self):
        # Main program loop
        while True :
            self.start_menu()
            choice = self.get_choice(1, 5)

            if choice == 1:
                # Add employee
                name, age, salary = self.get_emp_data()
                self.manager.add_emp(name, age, salary)

            elif choice == 2:
                # Print all employees
                employees = self.manager.get_employees()
                # Not an empty list
                if len(employees) != 0:
                    for emp in employees:
                        print(emp)
                else :
                    print('No employees yet')
                    
            elif choice == 3:
                # Delete employees by age range
                start, end = map(int, input('Enter age range Start, End : ').split())
                names = self.manager.delete_by_age(start, end)
                if len(names) != 0:
                    print(f'Deleting {' ,'.join(names)}')
                else:
                    print('No employee to delete!')

            elif choice == 4:
                # Update employee salary
                name = input('Enter employee name: ')
                salary = int(input('Enter new salary: '))
                state = self.manager.update_salary(name, salary)
                if state:
                    print(f'{name} salary updated successfully')
                else:
                    print('No such employee!')

            elif choice == 5:
                # Exit program
                break

if __name__ == '__main__':
    # Initialize Frontend and start main loop
    app = Frontend()
    app.run()