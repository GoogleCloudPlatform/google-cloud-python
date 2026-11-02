
transport inheritance structure
_______________________________

``SqlBackupsServiceTransport`` is the ABC for all transports.

- public child ``SqlBackupsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlBackupsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlBackupsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlBackupsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
