# Retry Strategy Conformance Testing

Calls fail for a host of transient reasons. In many cases the failures are ones that should be abstracted from customers, e.g. retryable issues. Retry strategies are included in the client library when it's safe to do so. These retry strategies are complex and need automated tests to ensure they work and continue to work in the future.

The Retry Strategy Conformance tests will ensure that retries are aligned across languages and operations are retried as specified.

## Test Suite Overview

The Retry Strategy Conformance tests leverage the conformance tests defined in [googleapis/conformance-tests](https://github.com/googleapis/conformance-tests/blob/master/storage/v1/retry_tests.json) to ensure adherence to expected behaviors.

The test suite uses the [storage-testbench](https://github.com/googleapis/storage-testbench)
to configure and generate tests cases which use fault injection to ensure conformance.

## Running the Conformance Test Suite

#### Prerequisites
1. Python 3.8
2. Nox
3. Docker

The Retry Strategy Conformance test suite is included in [`noxfile.py`](https://github.com/googleapis/python-storage/blob/main/noxfile.py) and run automatically as part of the Kokoro presubmits:
1. Running the testbench server via docker
2. Setup, validation, cleanup of individual test cases with the testbench
3. Test logs included in Kokoro build

To run the test suite locally:
```bash
nox -s conftest_retry-3.8
```

To run a single test locally:

Single test names are displayed as "test-S{scenario_id}-{method}-{client-library-method-name}-{instructions index}", such as `test-S1-storage.buckets.get-bucket_reload-1`

```bash
nox -re conftest_retry-3.8 -- -k <single_test_name>
```
