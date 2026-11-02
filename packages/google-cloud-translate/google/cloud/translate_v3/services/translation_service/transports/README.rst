
transport inheritance structure
_______________________________

``TranslationServiceTransport`` is the ABC for all transports.

- public child ``TranslationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TranslationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTranslationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TranslationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
