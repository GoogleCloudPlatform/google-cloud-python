
transport inheritance structure
_______________________________

``BigtableTransport`` is the ABC for all transports.

- public child ``BigtableGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BigtableGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBigtableRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BigtableRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
