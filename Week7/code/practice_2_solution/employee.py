class Employee:
    def __init__(self, name, employee_id):
        """
        Initialize a generic employee with basic information.

        Input:
        - name (str): The name of the employee.
        - employee_id (int): The unique ID of the employee.

        Output: None
        """
        self.name = name
        self.employee_id = employee_id
        self.performance_rating = None
        self.status = "Active"  # Status can be "Active", "On Leave", "Terminated"
        self.benefits = {"Health Insurance": False, "Retirement Plan": False}

    def calculate_salary(self):
        """
        Calculate the salary of the employee.
        This is a placeholder method intended to be overridden in derived classes.

        Input: None

        Output:
        - int: Base salary, default is 0.
        """
        return 0

    def set_performance_rating(self, rating):
        """
        Set the performance rating for the employee.

        Input:
        - rating (int): The performance rating of the employee.

        Output: None
        """
        pass

    def adjust_salary(self, adjustment):
        """
        Adjust the employee's salary.
        This method is intended to be overridden in derived classes where salary adjustments are applicable.

        Input:
        - adjustment (int): The amount by which to adjust the salary (positive or negative).

        Output: None
        """
        pass

    def update_status(self, new_status):
        """
        Update the employee's status.

        Input:
        - new_status (str): The new status of the employee (e.g., "Active", "On Leave", "Terminated").

        Output:
        - Prints the updated status of the employee.
        """
        print(f"{self.name}'s status has been updated to {new_status}.")
        self.status = new_status

    def add_benefit(self, benefit_name):
        """
        Add a benefit to the employee's benefits package.

        Input:
        - benefit_name (str): The name of the benefit to add.

        Output:
        - Prints the benefit addition status.
        """
        if benefit_name in self.benefits:
            self.benefits[benefit_name] = True
            print(f"{self.name} has been enrolled in {benefit_name}.")
        else:
            print(f"{benefit_name} is not available for enrollment.")

    def display_info(self):
        """
        Display the basic information of the employee.

        Input: None

        Output:
        - Prints the employee's name, ID, calculated salary, performance rating, status, and benefits.
        """
        print(f"Employee Name: {self.name}, ID: {self.employee_id}")
        print(f"Calculated Salary: {self.calculate_salary()}")
        print(f"Performance Rating: {self.performance_rating}")
        print(f"Status: {self.status}")
        print(f"Benefits: {self.benefits}")
