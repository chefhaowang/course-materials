class Employee:
    def __init__(self, name, employee_id):
        """
        Initialize the base attributes for an employee.
        :param name: Name of the employee
        :param employee_id: Unique ID of the employee
        """
        pass

    def calculate_salary(self):
        """
        Calculate the salary for the employee.
        This method should be overridden in derived classes to provide specific salary calculations.
        :return: Calculated salary
        """
        return 0

    def display_info(self):
        """
        Display the employee's information, including their name, ID, and calculated salary.
        :output: Printed information of the employee
        """
        print(f"Employee Name: {self.name}, ID: {self.employee_id}")
        print(f"Calculated Salary: {self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        """
        Initialize a full-time employee with name, ID, and annual salary.
        :param name: Name of the full-time employee
        :param employee_id: Unique ID of the employee
        :param annual_salary: The annual salary of the employee
        """
        pass

    def calculate_salary(self):
        """
        Calculate the monthly salary for a full-time employee.
        :return: Monthly salary calculated from the annual salary
        """
        pass


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        """
        Initialize a part-time employee with name, ID, hourly rate, and hours worked.
        :param name: Name of the part-time employee
        :param employee_id: Unique ID of the employee
        :param hourly_rate: Hourly wage of the employee
        :param hours_worked: Total hours worked by the employee
        """
        pass

    def calculate_salary(self):
        """
        Calculate the salary for a part-time employee based on hours worked.
        :return: Total salary based on hourly rate and hours worked
        """
        pass


class Contractor(Employee):
    def __init__(self, name, employee_id, contract_amount):
        """
        Initialize a contractor with name, ID, and contract amount.
        :param name: Name of the contractor
        :param employee_id: Unique ID of the contractor
        :param contract_amount: The fixed contract amount for the contractor
        """
        pass

    def calculate_salary(self):
        """
        Calculate the salary for a contractor.
        Contractors typically have a fixed contract amount, so this method returns that amount.
        :return: The contract amount as the salary
        """
        pass



def display_all_employees(employees):
    """
    Display information for all employees in the list.
    Calls the display_info() method for each employee to print their details.
    :param employees: List of employee objects
    :output: Printed information of all employees in the list
    """
    for employee in employees:
        employee.display_info()
        print("-" * 30)


if __name__ == "__main__":
    employees = [
        FullTimeEmployee("Alice", 1001, 60000),
        PartTimeEmployee("Bob", 1002, 20, 80),
        Contractor("Charlie", 1003, 5000),
    ]

    # Display all employees
    display_all_employees(employees)
