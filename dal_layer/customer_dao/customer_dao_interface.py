from abc import ABC, abstractmethod
from entities.customer_class_info import Customer


class CustomerDAOInterface(ABC):
    # Create
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass


