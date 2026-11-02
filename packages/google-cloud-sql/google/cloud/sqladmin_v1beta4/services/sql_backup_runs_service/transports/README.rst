
transport inheritance structure
_______________________________

``SqlBackupRunsServiceTransport`` is the ABC for all transports.

- public child ``SqlBackupRunsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlBackupRunsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlBackupRunsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlBackupRunsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
