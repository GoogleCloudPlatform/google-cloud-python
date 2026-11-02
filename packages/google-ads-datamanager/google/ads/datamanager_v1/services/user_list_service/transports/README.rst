
transport inheritance structure
_______________________________

``UserListServiceTransport`` is the ABC for all transports.

- public child ``UserListServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UserListServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUserListServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UserListServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
