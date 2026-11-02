
transport inheritance structure
_______________________________

``AuthorizedDomainsTransport`` is the ABC for all transports.

- public child ``AuthorizedDomainsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AuthorizedDomainsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAuthorizedDomainsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AuthorizedDomainsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
