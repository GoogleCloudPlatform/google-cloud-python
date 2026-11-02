
transport inheritance structure
_______________________________

``StoragePoolsTransport`` is the ABC for all transports.

- public child ``StoragePoolsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StoragePoolsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStoragePoolsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StoragePoolsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
