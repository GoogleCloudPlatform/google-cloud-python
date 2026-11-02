# CBT Python Test Proxy

The CBT test proxy is intended for running conformance tests for Cloud Bigtable Python Client.

## Option 1: Run Tests with Nox

You can run the conformance tests in a single line by calling `nox -s conformance` from the repo root


```
cd python-bigtable
nox -s conformance
```

## Option 2: Run processes manually

### Start test proxy

You can use `test_proxy.py` to launch a new test proxy process directly

```
cd python-bigtable/test_proxy
python test_proxy.py
```

The port can be set by passing in an extra positional argument

```
cd python-bigtable/test_proxy
python test_proxy.py --port 8080
```

By default, the test_proxy targets the async client. You can change this by passing in the `--client_type` flag.
Valid options are `async`, `sync`, and `legacy`.

```
python test_proxy.py --client_type=legacy
```

### Run the test cases

Prerequisites:
- If you have not already done so, [install golang](https://go.dev/doc/install).
- Before running tests, [launch an instance of the test proxy](#start-test-proxy) 
in a separate shell session, and make note of the port


Clone and navigate to the go test library:

```
git clone https://github.com/googleapis/cloud-bigtable-clients-test.git
cd cloud-bigtable-clients-test/tests
```


Launch the tests

```
go test -v -proxy_addr=:50055
```

