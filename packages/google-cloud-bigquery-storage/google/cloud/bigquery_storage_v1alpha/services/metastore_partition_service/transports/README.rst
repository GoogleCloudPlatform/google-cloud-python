
transport inheritance structure
_______________________________

``MetastorePartitionServiceTransport`` is the ABC for all transports.

- public child ``MetastorePartitionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MetastorePartitionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMetastorePartitionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MetastorePartitionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
