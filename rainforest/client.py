from .models import TestRun

import json
import requests

class RainforestError(Exception):
    pass

class Rainforest(object):
    """
    A client to interact with the RainforestQA API

    :param str client_token: Your account's API Client Token
    """
    def __init__(self, client_token, base_url='https://app.rainforestqa.com/api/1'):
        self.client_token = client_token
        self.base_url = base_url

    def run_tests(self, test_ids = None):
        """
        Invoke a test run for an array of test ids

        :param test_ids: An array of test ids to run or the string "all" to run all tests
        """
        r = requests.post(self.base_url + '/runs', data=json.dumps({
            'tests': test_ids
        }), headers={
            'Content-Type'  : 'application/json',
            'Accept'        : 'application/json',
            'CLIENT_TOKEN'  : self.client_token,
        })

        json_response = r.json()

        if r.status_code != 201:
            raise RainforestError(json_response.get('error', 'Unknown error has occurred'))

        return TestRun(
            id                  = json_response.get('id'), 
            object              = json_response.get('object'),
            created_at          = json_response.get('created_at'),
            environment_id      = json_response.get('environment_id'),
            state               = json_response.get('state'),
            result              = json_response.get('result'),
            expected_wait_time  = json_response.get('expected_wait_time'),
            browsers            = json_response.get('browsers'),
            requested_tests     = json_response.get('requested_tests'),
        )