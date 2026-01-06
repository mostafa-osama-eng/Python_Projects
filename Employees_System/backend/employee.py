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