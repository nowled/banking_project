class Customer:

    def __init__(self, customer_id: int, bank_id: int, first_name: str, last_name: str, account_number: int):
        self.customer_id = customer_id
        self.bank_id = bank_id
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name


"""
what do customers need to have to open and use a bank account

Customer first and last names may not exceed 20 characters
Customers must have unique Ids
"""
