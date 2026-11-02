
transport inheritance structure
_______________________________

``RegionInstancesTransport`` is the ABC for all transports.

- public child ``RegionInstancesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionInstancesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionInstancesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionInstancesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
