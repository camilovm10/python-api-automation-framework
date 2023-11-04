import json
import os.path
import logging as log

from mahar_group.src.dao.orders_dao import OrdersDAO
from mahar_group.src.utilities.requests_utility import RequestsUtility


class OrdersHelper:

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self._requests_utility = RequestsUtility()

    def create_order(self, additional_args=None):
        payload_path = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_path) as f:
            payload = json.load(f)

        # If user adds more info to payload, the update it
        if additional_args:
            assert isinstance(additional_args,
                              dict), f"Parameter 'additonal_args' must be a dictionary but found {type(additional_args)}"
            payload.update(additional_args)

        log.info(f"UPDATED PAYLOAD = {payload}")

        return self._requests_utility.post('orders', payload=payload)

    def verify_order_is_created(self, order_json, exp_cust_id, exp_products):

        orders_dao = OrdersDAO()

        customer_api_id = order_json['customer_id']
        orders_quantity = len(order_json['line_items'])

        assert exp_cust_id == customer_api_id, f"Create order should be '{exp_cust_id}', but got '{customer_api_id}'"
        assert orders_quantity == 1, f"Expected only '{len(exp_products)}' item in the order but got '{orders_quantity}'"

        order_id = order_json['id']
        order_db_info = orders_dao.get_order_by_id(order_id)

        line_items = [i for i in order_db_info if i['order_item_type'] == 'line_item']
        line_items_quantity = len(line_items)
        assert line_items_quantity == 1, f"Expected 1 line item but found '{line_items_quantity}'. Order Id: {order_id}"

        # Get list of product ids in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            product_id = product['product_id']
            assert product_id in api_product_ids, f"Order does not have at least 1 expected product in DB. Product Id: {product_id}. Order Id: {order_id}"

    def update_an_order(self, order_id, payload):

        return self._requests_utility.put(f'orders/{order_id}', payload=payload)

    def get_order_by_id(self, order_id):

        return self._requests_utility.get(f'orders/{order_id}')
