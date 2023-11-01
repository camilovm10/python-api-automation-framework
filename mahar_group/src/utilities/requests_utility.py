import json
import os
import requests
from mahar_group.src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
import logging as log

from mahar_group.src.utilities.credentials_utility import CredentialsUtility


class RequestsUtility:

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.status_code = None
        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds['wc_key'],
                           wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Expected status code '{self.expected_status_code}' but got '{self.status_code}'" \
                                                              f"URL: {self.url}, Response JSON: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        
        assert self.status_code == int(expected_status_code), f"Expected status code '{expected_status_code}' but got '{self.status_code}'"
        log.info(f"API POST response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        assert self.status_code == int(
            expected_status_code), f"Expected status code '{expected_status_code}' but got '{self.status_code}'"
        log.info(f"API GET response: {self.rs_json}")

        return self.rs_json