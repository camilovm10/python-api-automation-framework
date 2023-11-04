import random

from mahar_group.src.utilities.db_utility import DBUtility


class ProductsDAO:

    def __init__(self):
        self._db_helper = DBUtility()

    def get_random_product(self, qty=1):

        sql = "SELECT * FROM coolsite.wp_posts WHERE post_type = 'product' limit 5000;"
        rs_sql = self._db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):

        sql = f"SELECT * FROM coolsite.wp_posts WHERE ID = {product_id};"

        return self._db_helper.execute_select(sql)

    def get_product_after_given_date(self, _date):

        sql = f'SELECT * FROM coolsite.wp_posts WHERE post_type = "product" AND post_date > "{_date}" limit 10000;'

        return self._db_helper.execute_select(sql)