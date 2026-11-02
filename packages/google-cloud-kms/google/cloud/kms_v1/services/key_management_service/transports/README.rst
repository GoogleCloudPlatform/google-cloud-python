
transport inheritance structure
_______________________________

``KeyManagementServiceTransport`` is the ABC for all transports.

- public child ``KeyManagementServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``KeyManagementServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseKeyManagementServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``KeyManagementServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
