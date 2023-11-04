import pytest

from mahar_group.src.helpers.orders_helper import OrdersHelper


@pytest.mark.tcid55
def test_update_order_status():

    order_helper = OrdersHelper()

    new_status = 'cancelled'

    # Create new order
    order_json = order_helper.create_order()
    cur_status = order_json['status']

    assert cur_status != new_status, f"Current status of order is already '{new_status}'"

    # Update the status
    order_id = order_json['id']
    payload = {"status": new_status}

    order_helper.update_an_order(order_id, payload)
    new_order_info = order_helper.get_order_by_id(order_id)
    new_order_status = new_order_info['status']

    assert new_order_status == new_status, f"Updated order status to '{new_status}', but order status is '{new_order_status}'"

