
transport inheritance structure
_______________________________

``CertificateManagerTransport`` is the ABC for all transports.

- public child ``CertificateManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CertificateManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCertificateManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CertificateManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
