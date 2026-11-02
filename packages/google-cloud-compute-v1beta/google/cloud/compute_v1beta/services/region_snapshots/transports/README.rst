
transport inheritance structure
_______________________________

``RegionSnapshotsTransport`` is the ABC for all transports.

- public child ``RegionSnapshotsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionSnapshotsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionSnapshotsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionSnapshotsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
