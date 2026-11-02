
transport inheritance structure
_______________________________

``RegionTargetHttpProxiesTransport`` is the ABC for all transports.

- public child ``RegionTargetHttpProxiesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionTargetHttpProxiesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionTargetHttpProxiesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionTargetHttpProxiesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
