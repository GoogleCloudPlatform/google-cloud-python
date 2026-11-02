
transport inheritance structure
_______________________________

``TermsOfServiceAgreementStateServiceTransport`` is the ABC for all transports.

- public child ``TermsOfServiceAgreementStateServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TermsOfServiceAgreementStateServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTermsOfServiceAgreementStateServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TermsOfServiceAgreementStateServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
