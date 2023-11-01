import os


class CredentialsUtility:

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get("WC_KEY")
        wc_secret = os.environ.get("WC_SECRET")

        if not wc_key or not wc_secret:
            raise Exception("API credentials 'WC_KEY' and 'WC_SECRET' must be set as env variables")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():

        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
        db_port = os.environ.get("DB_PORT")
        db_host = os.environ.get("DB_HOST")

        if not db_user or not db_password or not db_port:
            raise Exception("DB credentials 'DB_USER', 'DB_PASSWORD', 'DB_PORT' and 'DB_HOST' must be set as env "
                            "variables")
        else:
            return {'db_user': db_user, 'db_password': db_password, 'db_port': db_port, 'db_host': db_host}
