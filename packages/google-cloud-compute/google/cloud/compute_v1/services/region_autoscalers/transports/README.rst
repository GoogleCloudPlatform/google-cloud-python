
transport inheritance structure
_______________________________

``RegionAutoscalersTransport`` is the ABC for all transports.

- public child ``RegionAutoscalersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionAutoscalersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionAutoscalersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionAutoscalersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
