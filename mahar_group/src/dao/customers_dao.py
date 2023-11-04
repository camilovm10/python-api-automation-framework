from mahar_group.src.utilities.db_utility import DBUtility
import logging as log
import random


class CustomersDAO:

    def __init__(self):
        self._db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM coolsite.wp_users WHERE user_email = '{email}';"
        log.debug(f"SQL statement: {sql}")
        return self._db_helper.execute_select(sql)

    def get_random_customer(self, qty=1):
        sql = f"SELECT * FROM coolsite.wp_users ORDER BY ID DESC LIMIT 5000;"
        log.debug(f"SQL statement: {sql}")
        rs_sql = self._db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))
