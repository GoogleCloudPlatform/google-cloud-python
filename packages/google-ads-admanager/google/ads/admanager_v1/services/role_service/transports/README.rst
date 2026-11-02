
transport inheritance structure
_______________________________

``RoleServiceTransport`` is the ABC for all transports.

- public child ``RoleServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RoleServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRoleServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RoleServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
