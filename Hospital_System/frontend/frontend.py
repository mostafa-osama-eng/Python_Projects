from backend.hospital_manager import HospitalManager
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
