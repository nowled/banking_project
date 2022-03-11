from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer


class CustomerDOIimp(CustomerDAOInterface):




    def create_customer(self, customer: Customer) -> Customer:

        last_name = 'Peterson'
        first_name = 'Charles'
        customer = 1
        first_name = customer.first_name
        last_name = customer.last_name
        customer = customer.customer_id
