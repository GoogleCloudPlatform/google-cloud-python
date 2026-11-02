
transport inheritance structure
_______________________________

``BigtableTableAdminTransport`` is the ABC for all transports.

- public child ``BigtableTableAdminGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BigtableTableAdminGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBigtableTableAdminRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BigtableTableAdminRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
