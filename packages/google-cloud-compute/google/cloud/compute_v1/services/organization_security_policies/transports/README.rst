
transport inheritance structure
_______________________________

``OrganizationSecurityPoliciesTransport`` is the ABC for all transports.

- public child ``OrganizationSecurityPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationSecurityPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationSecurityPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationSecurityPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
