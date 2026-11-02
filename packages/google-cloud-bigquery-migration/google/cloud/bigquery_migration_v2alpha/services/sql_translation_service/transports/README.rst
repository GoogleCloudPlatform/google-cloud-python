
transport inheritance structure
_______________________________

``SqlTranslationServiceTransport`` is the ABC for all transports.

- public child ``SqlTranslationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlTranslationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlTranslationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlTranslationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
