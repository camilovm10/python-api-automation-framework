import pytest
import logging as log

from mahar_group.src.helpers.customers_helper import CustomersHelper
from mahar_group.src.utilities.generic_utilities import generate_random_email_and_password
from mahar_group.src.dao.customers_dao import CustomersDAO
from mahar_group.src.utilities.requests_utility import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    log.info("TEST: Create new customer with email and password only")

    rand_credentials = generate_random_email_and_password()

    email = rand_credentials['email']
    password = rand_credentials['password']

    # Make API call
    cust_obj = CustomersHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # Verify firstname and email in the response
    assert cust_api_info['email'] == email, f"Create customer API call returned wrong email. Email '{email}'"
    assert cust_api_info['first_name'] == '', \
        f"Create customer API returned value for first_name when it should be empty"

    # Verify customer was created in the database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    cust_api_id = cust_api_info['id']
    cust_db_id = cust_info[0]['ID']

    assert cust_db_id == cust_api_id, f"API Customer response id '{cust_api_id}' is not the same as DB id '{cust_db_id}'"


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer()
    existing_email = existing_cust[0]['user_email']

    password = "Test1234"

    payload = {"email": existing_email, "password": password}

    # Make API call
    req_utility = RequestsUtility()
    cust_api_info = req_utility.post(endpoint="customers", payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', f"Registration email error message '{cust_api_info['code']}' is not correct"




