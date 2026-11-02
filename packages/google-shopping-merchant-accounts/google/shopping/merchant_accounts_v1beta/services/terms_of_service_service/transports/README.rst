
transport inheritance structure
_______________________________

``TermsOfServiceServiceTransport`` is the ABC for all transports.

- public child ``TermsOfServiceServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TermsOfServiceServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTermsOfServiceServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TermsOfServiceServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
