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
