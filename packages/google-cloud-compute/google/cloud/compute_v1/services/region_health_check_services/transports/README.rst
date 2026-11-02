
transport inheritance structure
_______________________________

``RegionHealthCheckServicesTransport`` is the ABC for all transports.

- public child ``RegionHealthCheckServicesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionHealthCheckServicesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionHealthCheckServicesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionHealthCheckServicesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
