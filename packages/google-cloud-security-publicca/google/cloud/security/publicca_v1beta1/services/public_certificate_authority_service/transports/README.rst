
transport inheritance structure
_______________________________

``PublicCertificateAuthorityServiceTransport`` is the ABC for all transports.

- public child ``PublicCertificateAuthorityServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PublicCertificateAuthorityServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePublicCertificateAuthorityServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PublicCertificateAuthorityServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
