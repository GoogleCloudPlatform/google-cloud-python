
transport inheritance structure
_______________________________

``BackupForGKETransport`` is the ABC for all transports.

- public child ``BackupForGKEGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BackupForGKEGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBackupForGKERestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BackupForGKERestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
