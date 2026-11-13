
transport inheritance structure
_______________________________

``OrganizationZoneVmExtensionPoliciesTransport`` is the ABC for all transports.

- public child ``OrganizationZoneVmExtensionPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationZoneVmExtensionPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationZoneVmExtensionPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationZoneVmExtensionPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
