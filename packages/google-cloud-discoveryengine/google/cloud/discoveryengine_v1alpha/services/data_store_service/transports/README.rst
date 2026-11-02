
transport inheritance structure
_______________________________

``DataStoreServiceTransport`` is the ABC for all transports.

- public child ``DataStoreServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataStoreServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataStoreServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataStoreServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
