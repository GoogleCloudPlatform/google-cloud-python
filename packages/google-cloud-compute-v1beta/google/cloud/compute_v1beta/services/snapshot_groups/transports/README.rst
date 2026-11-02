
transport inheritance structure
_______________________________

``SnapshotGroupsTransport`` is the ABC for all transports.

- public child ``SnapshotGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SnapshotGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSnapshotGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SnapshotGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
