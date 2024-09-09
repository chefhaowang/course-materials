from employee import Employee

class Intern(Employee):
    def __init__(self, name, employee_id, stipend, internship_duration_months):
        """
        Initialize an intern with a stipend and internship duration.
        
        Input:
        - name (str): The name of the intern.
        - employee_id (int): The unique ID of the intern.
        - stipend (int): The stipend amount provided to the intern.
        - internship_duration_months (int): The duration of the internship in months.
        
        Output: None
        """
        super().__init__(name, employee_id)
        self.stipend = stipend
        self.internship_duration_months = internship_duration_months  # Duration in months
        # Track the remaining months of the internship
        self.months_remaining = internship_duration_months
        self.mentor = None  # Initially, no mentor is assigned

    def calculate_salary(self):
        """
        Calculate the monthly stipend for the intern.
        
        Input: None
        
        Output:
        - int: The monthly stipend amount.
        """
        pass

    def assign_mentor(self, mentor_name):
        """
        Assign a mentor to the intern.
        
        Input:
        - mentor_name (str): The name of the mentor assigned to the intern.
        
        Output:
        - Prints the name of the assigned mentor.
        """
        pass

    def extend_internship(self, additional_months, additional_stipend):
        """
        Extend the duration of the internship and adjust the stipend.
        
        Input:
        - additional_months (int): The number of additional months to extend the internship.
        - additional_stipend (int): The additional stipend amount for the extended period.
        
        Output:
        - Prints the details of the internship extension.
        """
        pass

    def check_internship_status(self):
        """
        Check if the internship is nearing its end by evaluating the remaining months.
        
        Input: None
        
        Output:
        - Prints the remaining months or a warning if the internship is nearing its end.
        """
        pass
