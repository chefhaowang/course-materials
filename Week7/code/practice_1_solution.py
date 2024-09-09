class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        return 0 

    def display_info(self):
        print(f"Employee Name: {self.name}, ID: {self.employee_id}")
        print(f"Calculated Salary: {self.calculate_salary()}")



class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary / 12


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Contractor(Employee):
    def __init__(self, name, employee_id, contract_amount):
        super().__init__(name, employee_id)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount





def display_all_employees(employees):
    for employee in employees:
        employee.display_info()
        print("-" * 30)

if __name__ == "__main__":
    employees = [
        FullTimeEmployee("Alice", 1001, 60000),
        PartTimeEmployee("Bob", 1002, 20, 80),
        Contractor("Charlie", 1003, 5000),
    ]

    display_all_employees(employees)
