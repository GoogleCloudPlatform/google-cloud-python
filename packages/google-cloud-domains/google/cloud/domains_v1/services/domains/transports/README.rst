
transport inheritance structure
_______________________________

``DomainsTransport`` is the ABC for all transports.

- public child ``DomainsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DomainsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDomainsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DomainsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
