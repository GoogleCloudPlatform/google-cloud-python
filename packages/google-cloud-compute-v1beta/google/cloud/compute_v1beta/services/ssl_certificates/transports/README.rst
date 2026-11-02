
transport inheritance structure
_______________________________

``SslCertificatesTransport`` is the ABC for all transports.

- public child ``SslCertificatesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SslCertificatesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSslCertificatesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SslCertificatesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
