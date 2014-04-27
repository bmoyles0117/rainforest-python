# rainforest-python

A python module for interacting with the Rainforest API initiating tests and observing the progress of existing tests.

## Installation
After downloading the source, you can run the following command within the directory.

    python setup.py install

## Getting Started
To interact with the Rainforest API, simply create a Rainforest instance with your client token and you'll be ready to go!

    from rainforest import Rainforest

    client_token = 'a563************'
    client = Rainforest(client_token)

### Running Specific Tests
    from rainforest import Rainforest, RainforestError

    client_token = 'a563************'
    client = Rainforest(client_token)

    test_ids = [1,2]

    try:
        test_run = client.run_tests(test_ids)
        print "Test Run: %s" % (test_run.id, )
    except RainforestError, e:
        print "Failed to run tests: %s" % (e, )

### Running All Tests
    from rainforest import Rainforest, RainforestError

    client_token = 'a563************'
    client = Rainforest(client_token)

    try:
        test_run = client.run_tests(Rainforest.ALL_TESTS)
        print "Test Run: %s" % (test_run.id, )
    except RainforestError, e:
        print "Failed to run tests: %s" % (e, )
