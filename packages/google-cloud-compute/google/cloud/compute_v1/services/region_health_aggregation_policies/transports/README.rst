
transport inheritance structure
_______________________________

``RegionHealthAggregationPoliciesTransport`` is the ABC for all transports.

- public child ``RegionHealthAggregationPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionHealthAggregationPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionHealthAggregationPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionHealthAggregationPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
