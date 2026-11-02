
transport inheritance structure
_______________________________

``AuthorizedCertificatesTransport`` is the ABC for all transports.

- public child ``AuthorizedCertificatesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AuthorizedCertificatesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAuthorizedCertificatesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AuthorizedCertificatesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
