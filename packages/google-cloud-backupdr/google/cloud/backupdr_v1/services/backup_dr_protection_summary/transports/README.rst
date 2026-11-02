
transport inheritance structure
_______________________________

``BackupDrProtectionSummaryTransport`` is the ABC for all transports.

- public child ``BackupDrProtectionSummaryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BackupDrProtectionSummaryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBackupDrProtectionSummaryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BackupDrProtectionSummaryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
