from employee import Employee

class Contractor(Employee):
    def __init__(self, name, employee_id, contract_amount, contract_duration_months):
        """
        Initialize a contractor with a contract amount and duration.
        
        Input:
        - name (str): The name of the contractor.
        - employee_id (int): The unique ID of the contractor.
        - contract_amount (int): The total amount of the contract.
        - contract_duration_months (int): The duration of the contract in months.
        
        Output: None
        """
        super().__init__(name, employee_id)
        self.contract_amount = contract_amount
        self.contract_duration_months = contract_duration_months  # Duration in months
        # Track the remaining months of the contract
        self.months_remaining = contract_duration_months

    def calculate_salary(self):
        """
        Calculate the monthly payment for the contractor based on the total contract amount and duration.
        
        Input: None
        
        Output:
        - int: The monthly payment.
        """
        pass

    def renew_contract(self, additional_months, additional_amount):
        """
        Renew the contractor's contract by extending the duration and increasing the total amount.
        
        Input:
        - additional_months (int): The number of additional months to extend the contract.
        - additional_amount (int): The additional amount to add to the contract.
        
        Output:
        - Prints the details of the contract renewal.
        """
        pass

    def check_contract_status(self):
        """
        Check if the contract is nearing its end by evaluating the remaining months.
        
        Input: None
        
        Output:
        - Prints the remaining months or a warning if the contract is nearing its end.
        """
        pass
