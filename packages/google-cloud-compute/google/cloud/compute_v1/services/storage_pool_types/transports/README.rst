
transport inheritance structure
_______________________________

``StoragePoolTypesTransport`` is the ABC for all transports.

- public child ``StoragePoolTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StoragePoolTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStoragePoolTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StoragePoolTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
