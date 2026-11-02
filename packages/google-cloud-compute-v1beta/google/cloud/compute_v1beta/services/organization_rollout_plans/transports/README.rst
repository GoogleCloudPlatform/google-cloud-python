
transport inheritance structure
_______________________________

``OrganizationRolloutPlansTransport`` is the ABC for all transports.

- public child ``OrganizationRolloutPlansGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationRolloutPlansGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationRolloutPlansRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationRolloutPlansRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
