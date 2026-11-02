
transport inheritance structure
_______________________________

``SnapshotsTransport`` is the ABC for all transports.

- public child ``SnapshotsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SnapshotsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSnapshotsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SnapshotsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
