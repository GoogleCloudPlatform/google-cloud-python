
transport inheritance structure
_______________________________

``ConversationModelsTransport`` is the ABC for all transports.

- public child ``ConversationModelsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConversationModelsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConversationModelsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConversationModelsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
