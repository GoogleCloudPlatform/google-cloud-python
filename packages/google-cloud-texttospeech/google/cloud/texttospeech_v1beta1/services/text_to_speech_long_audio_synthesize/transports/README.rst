
transport inheritance structure
_______________________________

``TextToSpeechLongAudioSynthesizeTransport`` is the ABC for all transports.

- public child ``TextToSpeechLongAudioSynthesizeGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TextToSpeechLongAudioSynthesizeGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTextToSpeechLongAudioSynthesizeRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TextToSpeechLongAudioSynthesizeRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
