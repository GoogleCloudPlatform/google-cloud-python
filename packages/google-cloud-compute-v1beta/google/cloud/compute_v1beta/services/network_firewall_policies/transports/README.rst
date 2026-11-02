
transport inheritance structure
_______________________________

``NetworkFirewallPoliciesTransport`` is the ABC for all transports.

- public child ``NetworkFirewallPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkFirewallPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkFirewallPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkFirewallPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
