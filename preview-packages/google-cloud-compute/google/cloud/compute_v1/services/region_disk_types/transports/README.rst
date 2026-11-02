
transport inheritance structure
_______________________________

``RegionDiskTypesTransport`` is the ABC for all transports.

- public child ``RegionDiskTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionDiskTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionDiskTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionDiskTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
