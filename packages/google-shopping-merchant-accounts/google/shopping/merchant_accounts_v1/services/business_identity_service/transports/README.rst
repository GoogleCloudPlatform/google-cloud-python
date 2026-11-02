
transport inheritance structure
_______________________________

``BusinessIdentityServiceTransport`` is the ABC for all transports.

- public child ``BusinessIdentityServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BusinessIdentityServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBusinessIdentityServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BusinessIdentityServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
