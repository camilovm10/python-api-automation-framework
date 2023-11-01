import pytest
import logging as log

from mahar_group.src.dao.products_dao import ProductsDAO
from mahar_group.src.helpers.products_helper import ProductsHelper


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():

    req_helper = ProductsHelper()
    rs_api = req_helper.get_all_products()
    log.debug(f"Response of list all: {rs_api}")

    assert len(list(rs_api)) > 0, f"API call for products list is empty"


@pytest.mark.products
@pytest.mark.tcid25
def test_get_random_product():

    req_db = ProductsDAO().get_random_product()
    product_id_db = req_db[0]['ID']
    product_name_db = req_db[0]['post_title']

    req_helper = ProductsHelper()
    rs_api = req_helper.get_product_by_id(product_id_db)

    product_name_api = rs_api['id']

    assert product_name_api == product_name_db, f"Product name from API call '{product_name_api}' is not the same as " \
                                                f"DB '{product_name_db}'"