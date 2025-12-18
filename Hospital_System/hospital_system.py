"""
Hospital Queue Management System
Author: Mostafa Osama
Date: 2025-12-18
Description:
    A Python console application to manage hospital patient queues using OOP.
    Features:
    - Add new patients with priority handling (Normal, Urgent, Super Urgent)
    - List all patients per specialization
    - Serve the next patient according to priority
    - Remove patients from a specialization
"""
class Patient:
    """
    Represents a patient in the hospital system.

    Attributes:
        name (str): Patient full name
        status (int): Patient condition priority
                      0 -> Normal
                      1 -> Urgent
                      2 -> Super Urgent
        specialization (int): Medical specialization number (1-based)
    """
    def __init__(self, name, status, specialization):
        self.name = name
        self.status = status
        self.specialization = specialization

    def __str__(self):
        """
        User-friendly string representation used when printing a patient.
        """
        return f'Patient : {self.name} is {self.status}'
    
    def __repr__(self):
        """
        Developer-oriented representation useful for debugging.
        """
        return f'{self.name} his status is {self.status} and specialization is {self.specialization}'

class HospitalManager:
    """
    Handles all hospital logic:
    - Managing patient queues per specialization
    - Enforcing capacity limits
    - Handling patient priority ordering
    """
    def __init__(self):
        # Create a 2D list:
        # Each inner list represents a specialization queue
        # Total specializations = 20
        self.patients = [[] for _ in range(20)]

    def add_patient(self, name, status, specialization):
        """
        Adds a patient to the appropriate specialization queue
        while maintaining priority order.

        Priority rules:
            - Super urgent (2) patients are served first
            - Urgent (1) patients come after super urgent
            - Normal (0) patients come last

        Each specialization queue can hold up to 10 patients.

        Returns:
            bool: True if patient added successfully, False if specialization is full
        """
        # Convert specialization to zero-based index
        lst = self.patients[specialization - 1]
        # This specialization is full
        if len(lst) == 10 :
            return False
        # This specialization is empty
        elif len(lst) == 0:
            patient = Patient(name, status, specialization)
            lst.append(patient)
        else :
            patient = Patient(name, status, specialization)
            # Normal patient: always goes to the end
            if status == 0:
                lst.append(patient)
            # Urgent patient
            elif status == 1:
                # Insert after the last urgent or super urgent patient
                for idx in range(len(lst) - 1, -1, -1):
                    if lst[idx].status == 1 or lst[idx].status == 2:
                        lst.insert(idx + 1, patient)
                        break
                else:
                    # If no urgent or super urgent found, insert at front
                    lst.insert(0, patient)
            # Super urgent patient
            else:
                # Insert before normal or urgent patients
                for idx, p in enumerate(lst):
                    if p.status == 1:
                        lst.insert(idx, patient)
                        break
                    elif lst[idx].status == 2:
                        lst.insert(idx + 1, patient)
                        break

        return True

    def print_patients(self):
        """
        Returns a shallow copy of all specialization queues
        if there are any patients in the system.

        Returns:
            list | False: List of patients or False if no patients exist
        """
        # if there is any patient the condition'll be true
        if any(self.patients):
            return self.patients.copy()
        return False
    
    def get_next(self, specialization):
        """
        Retrieves and removes the next patient
        from a given specialization queue.

        Returns:
            Patient | False: Next patient or False if queue is empty
        """
        # holds the needed specialization
        sp = self.patients[specialization - 1]
        if len(sp) == 0:
            return False
        
        patient = sp[0]
        del sp[0]
        return patient
    
    def remove_patient(self, name, specialization):
        """
        Removes a patient by name from a specific specialization.

        Returns:
            bool: True if patient removed, False if not found
        """
        # holds the needed specialization
        sp = self.patients[specialization - 1]
        for idx, patient in enumerate(sp):
            if patient.name == name:
                del sp[idx]
                return True
        return False

class Frontend:
    """
    Handles user interaction:
    - Displays menus
    - Reads user input
    - Communicates with HospitalManager
    """
    def __init__(self):
        self.manager = HospitalManager()

    def print_menu(self):
        """
        Displays the main menu options.
        """
        menu = ['1: Add new patient', '2: Print all patients', '3: Get next patient',\
                '4: Remove a leaving patient', '5: End the program']
        print('\n'.join(menu))
    
    def get_choice(self):
        """
        Reads and validates menu choice.

        Returns:
            int | None: User choice or None if invalid
        """
        choice = int(input('Enter your choice from 1 to 5: '))
        if choice < 1 or choice > 5:
            return
        return choice

    def run(self):
        """
        Main program loop.
        """
        while True:
            self.print_menu()
            choice = self.get_choice()

            if choice == 1:
                # read patient data
                name = input('Enter patient name: ')
                status = int(input('Enter patient status: '))
                specialization = int(input('Enter patient specialization: '))

                if self.manager.add_patient(name, status, specialization):
                    print(f'{name} added successfully')
                else:
                    print('Sorry, no free space in this specialization')

            elif choice == 2:
                patients = self.manager.print_patients()
                if patients:
                    for specialization in patients:
                        for patient in specialization:
                            print(patient)
                else:
                    print('No patients yet')

            elif choice == 3:
                specialization = int(input('Enter the specialization: '))

                if patient := self.manager.get_next(specialization):
                    print(patient)
                else:
                    print('No patients in this specialization')

            elif choice == 4:
                name = input('Enter the patient name: ')
                specialization = int(input('Enter the patient specialization: '))

                if self.manager.remove_patient(name, specialization):
                    print(f'Patient {name} removed successfully')
                else:
                    print(f"The patient {name} doen't exist in this specialization {specialization}")
            elif choice == 5:
                print('Bye, See you later')
                break
            else:
                print('Invalid choice, Try again!')

if __name__ == '__main__':
    app = Frontend()
    app.run()
