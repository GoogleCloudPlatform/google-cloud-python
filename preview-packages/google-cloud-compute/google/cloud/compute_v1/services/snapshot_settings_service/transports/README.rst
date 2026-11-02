
transport inheritance structure
_______________________________

``SnapshotSettingsServiceTransport`` is the ABC for all transports.

- public child ``SnapshotSettingsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SnapshotSettingsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSnapshotSettingsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SnapshotSettingsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
