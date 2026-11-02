
transport inheritance structure
_______________________________

``MigrationServiceTransport`` is the ABC for all transports.

- public child ``MigrationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MigrationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMigrationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MigrationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
