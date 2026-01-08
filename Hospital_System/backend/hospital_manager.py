from backend.patient import Patient
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
