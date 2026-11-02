
transport inheritance structure
_______________________________

``SslPoliciesTransport`` is the ABC for all transports.

- public child ``SslPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SslPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSslPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SslPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
