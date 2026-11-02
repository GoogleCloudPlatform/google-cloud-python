
transport inheritance structure
_______________________________

``StorageControlTransport`` is the ABC for all transports.

- public child ``StorageControlGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StorageControlGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStorageControlRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StorageControlRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
