
transport inheritance structure
_______________________________

``RegionZonesTransport`` is the ABC for all transports.

- public child ``RegionZonesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionZonesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionZonesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionZonesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
