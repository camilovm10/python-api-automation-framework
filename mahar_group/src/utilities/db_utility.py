import pymysql
from mahar_group.src.utilities.credentials_utility import CredentialsUtility


class DBUtility:

    def __init__(self):
        self.creds = CredentialsUtility().get_db_credentials()
        pass

    def create_connection(self):

        connection = pymysql.connect(host=self.creds['db_host'], user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=int(self.creds['db_port']))

        return connection

    def execute_select(self, sql):

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
