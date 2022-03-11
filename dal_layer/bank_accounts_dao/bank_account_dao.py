from custom_exceptions.id_not_found import IdNotFound
from dal_layer.bank_accounts_dao.bank_accounts_interface_dao import BankAccountsInterface
from entities.bank_accounts_class import BankAccount


class BankAccountDAIimp(BankAccountsInterface):
    customer_list = []
    id_generator = 2

    def __init__(self):
        bank_id = 1
        customer_id = 1
        checking_account = 1
        savings_account = 1
        account_id_catch = BankAccount(bank_id, customer_id, checking_account, savings_account)
        self.customer_list.append(account_id_catch)

    def create_account(self, bank_account: BankAccount) -> BankAccount:
        bank_account.customer_id = self.id_generator
        self.id_generator += 1
        self.customer_list.append(bank_account)
        return bank_account

    # Read

    def get_account_by_id(self, customer_id: int, ) -> BankAccount:
        for bank_account in self.customer_list:
            if bank_account.customer_id == customer_id:
                return bank_account
            raise IdNotFound("Sorry Customer Id Not Found")

    # Read

    def get_all_accounts_for_user(self, customer_id: int, bank_account: BankAccount):

        pass

    def withdraw_from_account_by_id(self, account_id: int, bank_account: BankAccount):
        pass

    def deposit_into_account_by_id(self, account_id: int):
        pass

    def transfer_money_between_accounts_by_their_ids(self, bank_account: BankAccount):
        pass

    # Delete

    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                self.customer_list.remove(customer)
                return True
            raise IdNotFound("Sorry Customer Id Not Found")

    def delete_account_by_id(self,  bank: BankAccount) -> bool:
        for account in self.customer_list:
            if account.checking_account == bank.checking_account or account.savings_account == bank.savings_account:
                self.customer_list.remove(account)
                return True
            raise IdNotFound("Sorry Account Not Found")
