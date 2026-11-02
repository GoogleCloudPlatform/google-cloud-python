
transport inheritance structure
_______________________________

``SqlUsersServiceTransport`` is the ABC for all transports.

- public child ``SqlUsersServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlUsersServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlUsersServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlUsersServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
