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
        overtime_pay = self.overtime_hours * self.hourly_rate * 1.5
        return (self.hourly_rate * self.hours_worked) + overtime_pay

    def update_hours_worked(self, additional_hours):
        """
        Update the number of hours worked by the part-time employee, including tracking overtime.

        Input:
        - additional_hours (int): The number of additional hours worked.

        Output:
        - Prints the updated hours worked and overtime hours, if any.
        """
        regular_hours = min(40, self.hours_worked + additional_hours)
        self.overtime_hours += max(0, self.hours_worked +
                                   additional_hours - 40)
        self.hours_worked += additional_hours
        print(f"{self.name} worked an additional {additional_hours} hours. Total hours: {
              self.hours_worked} (Overtime: {self.overtime_hours} hours)")

    def adjust_salary(self, adjustment):
        """
        Adjust the employee's hourly rate.

        Input:
        - adjustment (int): The amount to adjust the hourly rate by.

        Output:
        - Prints the new hourly rate after adjustment.
        """
        self.hourly_rate += adjustment
        print(f"{self.name}'s hourly rate has been adjusted by {
              adjustment}. New hourly rate: {self.hourly_rate}")
