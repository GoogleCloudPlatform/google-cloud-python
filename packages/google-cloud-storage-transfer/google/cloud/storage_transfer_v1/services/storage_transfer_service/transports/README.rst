
transport inheritance structure
_______________________________

``StorageTransferServiceTransport`` is the ABC for all transports.

- public child ``StorageTransferServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StorageTransferServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStorageTransferServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StorageTransferServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
