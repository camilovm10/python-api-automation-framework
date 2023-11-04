import pytest
from datetime import datetime, timedelta
import logging as log

from mahar_group.src.dao.products_dao import ProductsDAO
from mahar_group.src.helpers.products_helper import ProductsHelper


@pytest.mark.regression
class TestListProductsWithFilter:

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        payload = dict()
        payload['after'] = after_created_date

        rs_api = ProductsHelper().get_all_products_with_payload(payload)

        assert rs_api, f"Empty response for 'list products with filter'"

        db_products = ProductsDAO().get_product_after_given_date(after_created_date)

        assert len(rs_api) == len(db_products), f"List products with filter 'after' returned unexpected number of " \
                                                f"products. Expected '{len(db_products)}, Actual: {len(rs_api)}'"

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        assert not ids_diff, f"List of API id products '{ids_in_api}' is different from the DB one '{ids_in_db}'"
