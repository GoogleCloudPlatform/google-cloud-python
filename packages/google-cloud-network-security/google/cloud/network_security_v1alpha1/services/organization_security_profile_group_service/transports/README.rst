
transport inheritance structure
_______________________________

``OrganizationSecurityProfileGroupServiceTransport`` is the ABC for all transports.

- public child ``OrganizationSecurityProfileGroupServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationSecurityProfileGroupServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationSecurityProfileGroupServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationSecurityProfileGroupServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
