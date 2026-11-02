
transport inheritance structure
_______________________________

``RegionHealthSourcesTransport`` is the ABC for all transports.

- public child ``RegionHealthSourcesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionHealthSourcesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionHealthSourcesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionHealthSourcesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
