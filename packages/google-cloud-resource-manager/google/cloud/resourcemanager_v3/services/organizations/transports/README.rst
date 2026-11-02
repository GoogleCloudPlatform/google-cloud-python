
transport inheritance structure
_______________________________

``OrganizationsTransport`` is the ABC for all transports.

- public child ``OrganizationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
