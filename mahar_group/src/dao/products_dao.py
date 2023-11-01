import random

from mahar_group.src.utilities.db_utility import DBUtility


class ProductsDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product(self, qty=1):

        sql = "SELECT * FROM coolsite.wp_posts WHERE post_type = 'product' limit 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))
