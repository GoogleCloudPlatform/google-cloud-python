
transport inheritance structure
_______________________________

``SecretManagerServiceTransport`` is the ABC for all transports.

- public child ``SecretManagerServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SecretManagerServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSecretManagerServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SecretManagerServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
