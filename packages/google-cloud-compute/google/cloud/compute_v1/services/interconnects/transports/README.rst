
transport inheritance structure
_______________________________

``InterconnectsTransport`` is the ABC for all transports.

- public child ``InterconnectsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InterconnectsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInterconnectsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InterconnectsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
