
transport inheritance structure
_______________________________

``CommentServiceTransport`` is the ABC for all transports.

- public child ``CommentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CommentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCommentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CommentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
