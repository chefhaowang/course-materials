from employee import Employee
from full_time_employee import FullTimeEmployee
from part_time_employee import PartTimeEmployee
from intern import Intern
from contractor import Contractor


def display_all_employees(employees):
    """
    Display the information for all employees in a list.
    
    Input:
    - employees (list): The list of employee objects to display.
    
    Output:
    - Prints the details of each employee in the list.
    """
    for employee in employees:
        employee.display_info()
        print("-" * 30)


def main():
    employees = [
        FullTimeEmployee("Alice", 1001, 60000),
        PartTimeEmployee("Bob", 1002, 20, 80),
        Contractor("Charlie", 1003, 5000, 6),
        Intern("David", 1004, 1500, 6),
    ]

    # Display all employees
    print("All Employees:")
    display_all_employees(employees)

    # Example: Promotion and Demotion for Full-Time Employee
    employees[0].promote(65000, 4)
    employees[0].take_vacation(5)
    employees[0].request_leave_of_absence(10)
    employees[0].adjust_salary(5000)

    # Example: Part-Time Employee Hours and Salary Adjustment
    employees[1].update_hours_worked(50)
    employees[1].adjust_salary(2)

    # Example: Contractor Contract Renewal and Status Check
    employees[2].renew_contract(3, 2000)
    employees[2].check_contract_status()

    # Example: Adding Benefits
    employees[0].add_benefit("Health Insurance")
    employees[1].add_benefit("Retirement Plan")

    # Example: Intern Mentor Assignment and Internship Extension
    employees[3].assign_mentor("John Doe")
    employees[3].extend_internship(2, 500)
    employees[3].check_internship_status()

    # Display all employees after changes
    print("All Employees After Changes:")
    display_all_employees(employees)


if __name__ == "__main__":
    main()
