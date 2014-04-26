from .client import Rainforest, requests
from mock import Mock
from .models import TestRun
from requests import Response
from unittest import TestCase

class TestRainforest(TestCase):
    def test_init(self):
        rainforest = Rainforest('CLIENT_TOKEN')

        self.assertEqual(rainforest.client_token, 'CLIENT_TOKEN')
        self.assertEqual(rainforest.base_url, 'https://app.rainforestqa.com/api/1')

    def test_run_tests(self):
        rainforest = Rainforest('CLIENT_TOKEN')

        mocked_response = Response()
        mocked_response.status_code = 201
        mocked_response._content = '{"id":1,"object":"Run","created_at":"2014-04-19T06:06:47Z","environment_id":1770,"state_log":[],"state":"queued","result":"no_result","expected_wait_time":8100.0,"browsers":[{"name":"chrome","state":"disabled"},{"name":"firefox","state":"disabled"},{"name":"ie8","state":"disabled"},{"name":"ie9","state":"disabled"},{"name":"safari","state":"disabled"}],"requested_tests":[1,2,3]}'

        requests.post = Mock(return_value=mocked_response)

        test_run = rainforest.run_tests([1,2,3])

        requests.post.assert_called_with('https://app.rainforestqa.com/api/1/runs', data='{"tests": [1, 2, 3]}', headers={
            'Content-Type'  : 'application/json',
            'Accept'        : 'application/json',
            'CLIENT_TOKEN'  : 'CLIENT_TOKEN',
        })

        self.assertIsInstance(test_run, TestRun)
        self.assertEqual(test_run.id, 1)
        self.assertEqual(test_run.object, 'Run')
        self.assertEqual(test_run.created_at, '2014-04-19T06:06:47Z')
        self.assertEqual(test_run.environment_id, 1770)
        self.assertEqual(test_run.state, 'queued')
        self.assertEqual(test_run.result, 'no_result')
        self.assertEqual(test_run.expected_wait_time, 8100.0)
        self.assertEqual(test_run.browsers, [{"name":"chrome","state":"disabled"},{"name":"firefox","state":"disabled"},{"name":"ie8","state":"disabled"},{"name":"ie9","state":"disabled"},{"name":"safari","state":"disabled"}])
        self.assertEqual(test_run.requested_tests, [1,2,3])