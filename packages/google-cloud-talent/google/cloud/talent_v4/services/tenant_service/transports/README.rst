
transport inheritance structure
_______________________________

``TenantServiceTransport`` is the ABC for all transports.

- public child ``TenantServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TenantServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTenantServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TenantServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
