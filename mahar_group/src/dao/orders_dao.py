from mahar_group.src.utilities.db_utility import DBUtility


class OrdersDAO:

    def __init__(self):
        self._db_helper = DBUtility()

    def get_order_by_id(self, order_id):
        sql = f"SELECT * FROM coolsite.wp_woocommerce_order_items WHERE order_id = {order_id};"

        return self._db_helper.execute_select(sql)

    def get_order_item_details(self, order_item_id):
        sql = f"SELECT * FROM coolsite.wp_woocommerce_order_itemmeta WHERE order_item_id = {order_item_id};"
        rs_sql = self._db_helper.execute_select(sql)
        line_details = dict()
        for meta in rs_sql:
            line_details[meta['meta_key']] = meta['meta_value']

        return line_details


