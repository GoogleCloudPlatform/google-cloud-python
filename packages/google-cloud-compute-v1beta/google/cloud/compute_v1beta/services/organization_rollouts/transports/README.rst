
transport inheritance structure
_______________________________

``OrganizationRolloutsTransport`` is the ABC for all transports.

- public child ``OrganizationRolloutsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationRolloutsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationRolloutsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationRolloutsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
