
transport inheritance structure
_______________________________

``SnapshotsV1Beta3Transport`` is the ABC for all transports.

- public child ``SnapshotsV1Beta3GrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SnapshotsV1Beta3GrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSnapshotsV1Beta3RestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SnapshotsV1Beta3RestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
