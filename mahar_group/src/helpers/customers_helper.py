from mahar_group.src.utilities.generic_utilities import generate_random_email_and_password
from mahar_group.src.utilities.requests_utility import RequestsUtility


class CustomersHelper:

    def __init__(self):
        self._requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            email = generate_random_email_and_password()['email']
        if not password:
            password = 'test1234'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        craete_user_json = self._requests_utility.post('customers', payload=payload,
                                                       expected_status_code=201)

        return craete_user_json

    def get_all_customers(self):
        return self._requests_utility.get('customers')
