
transport inheritance structure
_______________________________

``UserStoreServiceTransport`` is the ABC for all transports.

- public child ``UserStoreServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UserStoreServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUserStoreServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UserStoreServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
