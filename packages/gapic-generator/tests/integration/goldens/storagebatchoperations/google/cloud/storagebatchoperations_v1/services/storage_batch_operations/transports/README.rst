
transport inheritance structure
_______________________________

``StorageBatchOperationsTransport`` is the ABC for all transports.

- public child ``StorageBatchOperationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StorageBatchOperationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStorageBatchOperationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StorageBatchOperationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
