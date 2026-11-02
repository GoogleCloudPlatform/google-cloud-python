
transport inheritance structure
_______________________________

``RegionSnapshotSettingsTransport`` is the ABC for all transports.

- public child ``RegionSnapshotSettingsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionSnapshotSettingsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionSnapshotSettingsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionSnapshotSettingsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
