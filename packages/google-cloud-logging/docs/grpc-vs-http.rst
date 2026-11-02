gRPC vs HTTP
====================

:mod:`google-cloud-logging` supports two different protocols for sending logs over the network:
gRPC and HTTP. Both implementations conform to the same API, and should be
invisible to the end user.

gRPC is enabled by default. You can switch to HTTP mode by either:

- setting the `DISABLE_GRPC` environment variable to `TRUE`
- or, passing `_use_grpc=False` when initializing a Client

We recommend using gRPC whenever possible, but you may want to try the HTTP
implementation if you have network issues when using gRPC.
