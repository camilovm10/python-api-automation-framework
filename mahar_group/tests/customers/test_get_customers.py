import pytest
import logging as log

from mahar_group.src.helpers.customers_helper import CustomersHelper

@pytest.mark.tcid30
def test_get_all_costumers():

    req_helper = CustomersHelper()
    rs_api = req_helper.get_all_customers()
    log.debug(f"Response of list all: {rs_api}")

    assert len(list(rs_api)) > 0, f"API call for customers list is empty"
