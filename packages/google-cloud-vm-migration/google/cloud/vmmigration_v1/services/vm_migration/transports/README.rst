
transport inheritance structure
_______________________________

``VmMigrationTransport`` is the ABC for all transports.

- public child ``VmMigrationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VmMigrationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVmMigrationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VmMigrationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
