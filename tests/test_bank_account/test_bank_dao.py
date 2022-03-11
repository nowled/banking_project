from custom_exceptions.id_not_found import IdNotFound
from dal_layer.bank_accounts_dao.bank_account_dao import BankAccountDAIimp
from entities.bank_accounts_class import BankAccount

bank_account_dao = BankAccountDAIimp()

bank_id = 0
customer_id = 0
checking_account = 50
savings_account = 50
test_account = BankAccount(bank_id, customer_id, checking_account, savings_account)


def test_create_account_success():
    result = bank_account_dao.create_account(test_account)
    assert result.customer_id != 0


def test_non_unique_id():
    bank = 1
    customer = 1
    checking_accounts = 50
    savings_accounts = 50
    test_accounts = BankAccount(bank, customer, checking_accounts, savings_accounts)
    result = bank_account_dao.create_account(test_accounts)
    assert result.customer_id != 0


def test_get_account_by_id_success():
    result = bank_account_dao.get_account_by_id(1)
    assert result.customer_id == 1


def test_get_non_existent_customer_by_id():
    try:
        bank_account_dao.get_account_by_id(1000)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customers with that Id found"


def test_get_all_accounts_for_user():
    result = bank_account_dao.get_all_accounts_for_user(test_account.checking_account, test_account.savings_account)
    assert result.savings_account and result.checking_account != -1


def test_withdraw_from_account_by_id():
    pass


def test_deposit_into_account_by_id():
    pass


def test_transfer_money_between_accounts_by_their_ids():
    pass


def test_delete_customer_by_id_success():
    result = bank_account_dao.delete_customer_by_id(1)
    assert result


def test_delete_customer_nonexistent_id():
    try:
        bank_account_dao.delete_customer_by_id(1)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customers with that Id found"


def test_delete_account_by_id_success():
    result = bank_account_dao.delete_account_by_id(1)
    assert result


def test_delete_account_nonexistent_id():
    try:
        bank_account_dao.delete_account_by_id(1)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Account with that Id found"


"""

As a customer, I can create a new bank account with a starting balance so I have somewhere to store my money (create_account)
As a customer, I can view the balance of a specific account so I can check my finances (get_account_by_id)
as a customer, I can view the balance of all my accounts so I know exactly how much money I have (get_all_accounts_for_user)
As a customer, I can make a withdrawal from a specific account so I can have access to my money (withdraw_from_account_by_id)
As a customer, I can make a deposit to a specific account so I can store my money for safe keeping (deposit_into_account_by_id)
As a customer, I can transfer money between accounts so I can consolidate my money (transfer_money_between_accounts_by_their_ids)
As a customer, I can close any of my bank accounts so that it is easier to remember where my money resides (delete_account_by_id)
As a customer, I can end my relationship with the bank when it is no longer needed (delete_customer_by_id)

"""
