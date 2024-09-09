from employee import Employee

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        """
        Initialize a part-time employee with an hourly rate and hours worked.
        
        Input:
        - name (str): The name of the employee.
        - employee_id (int): The unique ID of the employee.
        - hourly_rate (int): The hourly rate for the employee.
        - hours_worked (int): The number of hours the employee has worked.
        
        Output: None
        """
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.overtime_hours = 0  # Initialize overtime hours to 0

    def calculate_salary(self):
        """
        Calculate the total salary of the part-time employee, including overtime pay.
        
        Input: None
        
        Output:
        - int: The total calculated salary.
        """
        pass

    def update_hours_worked(self, additional_hours):
        """
        Update the number of hours worked by the part-time employee, including tracking overtime.
        
        Input:
        - additional_hours (int): The number of additional hours worked.
        
        Output:
        - Prints the updated hours worked and overtime hours, if any.
        """
        pass

    def adjust_salary(self, adjustment):
        """
        Adjust the employee's hourly rate.
        
        Input:
        - adjustment (int): The amount to adjust the hourly rate by.
        
        Output:
        - Prints the new hourly rate after adjustment.
        """
        pass
