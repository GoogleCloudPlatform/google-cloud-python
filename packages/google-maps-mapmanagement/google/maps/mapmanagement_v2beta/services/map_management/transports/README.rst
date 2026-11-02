
transport inheritance structure
_______________________________

``MapManagementTransport`` is the ABC for all transports.

- public child ``MapManagementGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MapManagementGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMapManagementRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MapManagementRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
