
transport inheritance structure
_______________________________

``RegionMultiMigMembersTransport`` is the ABC for all transports.

- public child ``RegionMultiMigMembersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionMultiMigMembersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionMultiMigMembersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionMultiMigMembersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
