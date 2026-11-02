
transport inheritance structure
_______________________________

``RegionDisksTransport`` is the ABC for all transports.

- public child ``RegionDisksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionDisksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionDisksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionDisksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
