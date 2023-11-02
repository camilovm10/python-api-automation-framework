from mahar_group.src.utilities.requests_utility import RequestsUtility


class ProductsHelper:

    def __init__(self):
        self.req_utility = RequestsUtility()

    def get_all_products(self):
        return self.req_utility.get(endpoint="products", expected_status_code=200)

    def get_product_by_id(self, product_id):
        return self.req_utility.get(endpoint=f"products/{product_id}", expected_status_code=200)

    def create_product(self, payload):
        return self.req_utility.post(endpoint="products", payload=payload, expected_status_code=201)
