# imports
from backend.employee_manager import EmployeeManager
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
