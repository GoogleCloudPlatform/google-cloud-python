
transport inheritance structure
_______________________________

``BackupDRTransport`` is the ABC for all transports.

- public child ``BackupDRGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BackupDRGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBackupDRRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BackupDRRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
