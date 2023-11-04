import pytest

from mahar_group.src.dao.orders_dao import OrdersDAO
from mahar_group.src.dao.products_dao import ProductsDAO
from mahar_group.src.helpers.orders_helper import OrdersHelper
from mahar_group.src.helpers.customers_helper import CustomersHelper

pytestmark = [pytest.mark.orders]


@pytest.fixture
def my_orders_setup():
    product_dao = ProductsDAO()
    # Get a product from DB
    rand_product = product_dao.get_random_product(1)
    product_id = rand_product[0]['ID']
    return {'product_id': product_id}


@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_setup):
    # Create helper objects
    order_helper = OrdersHelper()
    customer_id = 0
    product_id = my_orders_setup['product_id']

    # Make API call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)

    # Assertions
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_setup):
    # Create helper objects
    order_helper = OrdersHelper()
    customer_helper = CustomersHelper()

    # Make API call
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']
    product_id = my_orders_setup['product_id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        "customer_id": customer_id
    }
    order_json = order_helper.create_order(additional_args=info)

    # Assertions
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)
