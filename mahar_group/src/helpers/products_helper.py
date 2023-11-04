from mahar_group.src.utilities.requests_utility import RequestsUtility
import logging as log

class ProductsHelper:

    def __init__(self):
        self._req_utility = RequestsUtility()

    def get_all_products(self):
        return self._req_utility.get(endpoint="products", expected_status_code=200)

    def get_all_products_with_payload(self, payload):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            log.debug(f"List products page number: {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            payload['page'] = i

            rs_api = self._req_utility.get(endpoint="products", payload=payload)

            if not rs_api:
                break
            else:
                all_products.extend(rs_api)

        # An else can be used for a for loop to be triggered in case a break is not hit. Will work as an 'except'
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages")

        return all_products

    def get_product_by_id(self, product_id):
        return self._req_utility.get(endpoint=f"products/{product_id}", expected_status_code=200)

    def create_product(self, payload):
        return self._req_utility.post(endpoint="products", payload=payload, expected_status_code=201)
