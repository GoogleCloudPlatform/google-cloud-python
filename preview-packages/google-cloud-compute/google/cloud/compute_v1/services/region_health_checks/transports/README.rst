
transport inheritance structure
_______________________________

``RegionHealthChecksTransport`` is the ABC for all transports.

- public child ``RegionHealthChecksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionHealthChecksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionHealthChecksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionHealthChecksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
