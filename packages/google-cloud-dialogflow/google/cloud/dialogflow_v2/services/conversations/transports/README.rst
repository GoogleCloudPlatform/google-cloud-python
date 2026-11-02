
transport inheritance structure
_______________________________

``ConversationsTransport`` is the ABC for all transports.

- public child ``ConversationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConversationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConversationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConversationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
