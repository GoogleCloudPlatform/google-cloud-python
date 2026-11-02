
transport inheritance structure
_______________________________

``DataMigrationServiceTransport`` is the ABC for all transports.

- public child ``DataMigrationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataMigrationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataMigrationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataMigrationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
