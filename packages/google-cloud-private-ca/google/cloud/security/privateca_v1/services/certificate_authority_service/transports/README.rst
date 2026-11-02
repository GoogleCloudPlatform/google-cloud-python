
transport inheritance structure
_______________________________

``CertificateAuthorityServiceTransport`` is the ABC for all transports.

- public child ``CertificateAuthorityServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CertificateAuthorityServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCertificateAuthorityServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CertificateAuthorityServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
