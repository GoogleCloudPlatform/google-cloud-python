Features and Limitations
------------------------

Nice things this client does:

- Implemented in pure Python, with language-idiomatic templating tools.
- It supports multiple transports: both gRPC and protobuf over HTTP/1.1.
  A JSON-based transport would be easy to add.
- It uses a lighter-weight configuration, specified in the protocol
  buffer itself.

As this is experimental work, please note the following limitations:

- The output only works on Python 3.5 and above.
- The configuration annotations are experimental and provided in
  `an awkward location`_.
- gRPC must be installed even if you are not using it (this is due to
  some minor issues in ``api-core``).
- No support for samples yet.

.. _an awkward location: https://github.com/googleapis/api-common-protos/blob/input-contract/google/api/
