
transport inheritance structure
_______________________________

``RegionSslPoliciesTransport`` is the ABC for all transports.

- public child ``RegionSslPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionSslPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionSslPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionSslPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
