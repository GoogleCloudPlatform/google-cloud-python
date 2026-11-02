
transport inheritance structure
_______________________________

``RegionNetworkFirewallPoliciesTransport`` is the ABC for all transports.

- public child ``RegionNetworkFirewallPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionNetworkFirewallPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionNetworkFirewallPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionNetworkFirewallPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
