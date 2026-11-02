
transport inheritance structure
_______________________________

``TextToSpeechTransport`` is the ABC for all transports.

- public child ``TextToSpeechGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TextToSpeechGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTextToSpeechRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TextToSpeechRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
