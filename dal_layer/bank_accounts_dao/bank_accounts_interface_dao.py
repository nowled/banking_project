from abc import ABC, abstractmethod

from entities.bank_accounts_class import BankAccount


class BankAccountsInterface(ABC):

    @abstractmethod
    def create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    # Read
    @abstractmethod
    def get_account_by_id(self, customer_id: int, bank_account: BankAccount) -> BankAccount:
        pass

    # Read
    @abstractmethod
    def get_all_accounts_for_user(self, customer_id: int,  bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, account_id: int, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, bank_account: BankAccount) -> BankAccount:
        pass

    # Delete
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def delete_account_by_id(self, customer_id: int, bank: BankAccount) -> bool:
        pass


"""
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
