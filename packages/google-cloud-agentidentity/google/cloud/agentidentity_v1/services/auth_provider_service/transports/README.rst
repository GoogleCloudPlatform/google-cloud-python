
transport inheritance structure
_______________________________

``AuthProviderServiceTransport`` is the ABC for all transports.

- public child ``AuthProviderServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AuthProviderServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAuthProviderServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AuthProviderServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
