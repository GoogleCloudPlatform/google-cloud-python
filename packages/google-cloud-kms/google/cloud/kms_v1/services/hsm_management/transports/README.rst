
transport inheritance structure
_______________________________

``HsmManagementTransport`` is the ABC for all transports.

- public child ``HsmManagementGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HsmManagementGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHsmManagementRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HsmManagementRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
