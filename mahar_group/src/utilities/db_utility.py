import os
import logging as log
import pymysql

from mahar_group.src.configs.hosts_config import DB_HOSTS
from mahar_group.src.utilities.credentials_utility import CredentialsUtility


class DBUtility:

    def __init__(self):
        self._creds = CredentialsUtility().get_db_credentials()

        machine = os.environ.get('MACHINE')
        assert machine, "Environment machine must be set"

        env = os.environ.get('ENV', 'test')

        self.host = DB_HOSTS[machine][env]['host']
        self.port = DB_HOSTS[machine][env]['port']

    def create_connection(self):

        connection = pymysql.connect(host=self.host, user=self._creds['db_user'],
                                     password=self._creds['db_password'], port=int(self.port))

        return connection

    def execute_select(self, sql):

        log.info(f"Running SQL: {sql}")
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)

            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql} . Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass
