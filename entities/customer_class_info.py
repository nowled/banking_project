class Customer:

    def __init__(self, customer_id: int, bank_id: int, first_name: str, last_name: str, checking_account: int, savings_account: int):
        self.customer_id = customer_id
        self.bank_id = bank_id
        self.checking_account = checking_account
        self.savings_account = savings_account
        self.first_name = first_name
        self.last_name = last_name


"""
what do customers need to have to open and use a bank account

Customer first and last names may not exceed 20 characters
Customers must have unique Ids
As a customer, I can start a business relationship with the bank so I can store my money securely(create_customer)
As a customer, I can create a new bank account with a starting balance so I have somewhere to store my money (create_account)
As a customer, I can view the balance of a specific account so I can check my finances (get_account_by_id)
as a customer, I can view the balance of all my accounts so I know exactly how much money I have (get_all_accounts_for_user)
As a customer, I can make a withdrawal from a specific account so I can have access to my money (withdraw_from_account_by_id)
As a customer, I can make a deposit to a specific account so I can store my money for safe keeping (deposit_into_account_by_id)
As a customer, I can transfer money between accounts so I can consolidate my money (transfer_money_between_accounts_by_their_ids)
As a customer, I can close any of my bank accounts so that it is easier to remember where my money resides (delete_account_by_id)
As a customer, I can end my relationship with the bank when it is no longer needed (delete_customer_by_id)

"""
