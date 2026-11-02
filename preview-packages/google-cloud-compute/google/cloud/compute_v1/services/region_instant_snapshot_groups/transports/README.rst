
transport inheritance structure
_______________________________

``RegionInstantSnapshotGroupsTransport`` is the ABC for all transports.

- public child ``RegionInstantSnapshotGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionInstantSnapshotGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionInstantSnapshotGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionInstantSnapshotGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
