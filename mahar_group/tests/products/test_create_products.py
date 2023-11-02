import pytest

from mahar_group.src.utilities.generic_utilities import generate_random_string
from mahar_group.src.helpers.products_helper import ProductsHelper
from mahar_group.src.dao.products_dao import ProductsDAO


@pytest.mark.tcid26
def test_create_simple_product():

    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "18.95"

    products_rs = ProductsHelper().create_product(payload)

    product_name_api = products_rs['name']
    product_name = payload['name']

    assert product_name_api == product_name, f"Product name from API '{product_name_api}' does not match the one " \
                                                f"created '{product_name}' "

    product_id = products_rs['id']
    product_db = ProductsDAO().get_product_by_id(product_id)
    product_db_name = product_db[0]['post_title']

    assert product_name == product_db_name, f"Product from DB has a name '{product_db_name}' different than the one " \
                                            f"used for creation '{product_name}' "

