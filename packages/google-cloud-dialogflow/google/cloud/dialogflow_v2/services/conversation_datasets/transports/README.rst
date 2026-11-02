
transport inheritance structure
_______________________________

``ConversationDatasetsTransport`` is the ABC for all transports.

- public child ``ConversationDatasetsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConversationDatasetsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConversationDatasetsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConversationDatasetsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
