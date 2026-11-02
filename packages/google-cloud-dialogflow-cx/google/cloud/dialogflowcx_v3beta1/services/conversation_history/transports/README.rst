
transport inheritance structure
_______________________________

``ConversationHistoryTransport`` is the ABC for all transports.

- public child ``ConversationHistoryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConversationHistoryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConversationHistoryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConversationHistoryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
