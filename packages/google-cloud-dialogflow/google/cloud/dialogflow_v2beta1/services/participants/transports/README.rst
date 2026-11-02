
transport inheritance structure
_______________________________

``ParticipantsTransport`` is the ABC for all transports.

- public child ``ParticipantsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ParticipantsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseParticipantsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ParticipantsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
