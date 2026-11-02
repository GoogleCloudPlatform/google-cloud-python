
transport inheritance structure
_______________________________

``RegionNetworkPoliciesTransport`` is the ABC for all transports.

- public child ``RegionNetworkPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionNetworkPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionNetworkPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionNetworkPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
