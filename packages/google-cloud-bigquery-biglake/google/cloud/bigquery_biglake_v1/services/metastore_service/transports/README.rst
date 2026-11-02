
transport inheritance structure
_______________________________

``MetastoreServiceTransport`` is the ABC for all transports.

- public child ``MetastoreServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MetastoreServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMetastoreServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MetastoreServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
