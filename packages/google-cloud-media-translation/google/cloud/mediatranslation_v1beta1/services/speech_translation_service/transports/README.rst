
transport inheritance structure
_______________________________

``SpeechTranslationServiceTransport`` is the ABC for all transports.

- public child ``SpeechTranslationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SpeechTranslationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSpeechTranslationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SpeechTranslationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
