
transport inheritance structure
_______________________________

``AuthProviderCredentialsServiceTransport`` is the ABC for all transports.

- public child ``AuthProviderCredentialsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AuthProviderCredentialsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAuthProviderCredentialsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AuthProviderCredentialsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
