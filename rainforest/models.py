from collections import namedtuple

TestRun = namedtuple('TestRun', 'id object created_at environment_id \
    state result expected_wait_time browsers requested_tests')