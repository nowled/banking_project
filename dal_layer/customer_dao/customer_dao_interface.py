from abc import ABC, abstractmethod
from entities.customer_class_info import Customer


class CustomerDAOInterface(ABC):
    # Create
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # Read
    @abstractmethod
    def get_account_by_id(self, account_number: int, customer_id: int) -> Customer:
        pass

    # Update
    @abstractmethod
    def update_account_by_id(self, customer: Customer) -> Customer:
        pass

    # Delete
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
