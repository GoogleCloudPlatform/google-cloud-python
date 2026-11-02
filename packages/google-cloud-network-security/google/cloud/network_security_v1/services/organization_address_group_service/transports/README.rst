
transport inheritance structure
_______________________________

``OrganizationAddressGroupServiceTransport`` is the ABC for all transports.

- public child ``OrganizationAddressGroupServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrganizationAddressGroupServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrganizationAddressGroupServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrganizationAddressGroupServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
