from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        """
        Initialize a full-time employee with an annual salary and vacation days.
        
        Input:
        - name (str): The name of the employee.
        - employee_id (int): The unique ID of the employee.
        - annual_salary (int): The annual salary of the employee.
        
        Output: None
        """
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary
        self.vacation_days = 20  # Default vacation days for full-time employees

    def calculate_salary(self):
        """
        Calculate the monthly salary of the full-time employee based on the annual salary.
        
        Input: None
        
        Output:
        - int: The monthly salary.
        """
        pass

    def promote(self, new_annual_salary, new_performance_rating=None):
        """
        Promote the employee by increasing the annual salary and optionally updating the performance rating.
        
        Input:
        - new_annual_salary (int): The new annual salary after promotion.
        - new_performance_rating (int, optional): The new performance rating (optional).
        
        Output:
        - Prints the promotion details.
        """
        pass

    def demote(self, new_annual_salary, new_performance_rating=None):
        """
        Demote the employee by decreasing the annual salary and optionally updating the performance rating.
        
        Input:
        - new_annual_salary (int): The new annual salary after demotion.
        - new_performance_rating (int, optional): The new performance rating (optional).
        
        Output:
        - Prints the demotion details.
        """
        pass

    def adjust_salary(self, adjustment):
        """
        Adjust the employee's annual salary.
        
        Input:
        - adjustment (int): The amount to adjust the salary by (positive for raise, negative for cut).
        
        Output:
        - Prints the salary adjustment details.
        """
        pass

    def take_vacation(self, days):
        """
        Deduct vacation days from the employee's available vacation days.
        
        Input:
        - days (int): The number of vacation days to take.
        
        Output:
        - Prints the remaining vacation days after the deduction.
        """
        pass

    def request_leave_of_absence(self, leave_days):
        """
        Request leave of absence for a number of days.
        
        Input:
        - leave_days (int): The number of days of leave requested.
        
        Output:
        - Prints the leave request status.
        """
        pass
