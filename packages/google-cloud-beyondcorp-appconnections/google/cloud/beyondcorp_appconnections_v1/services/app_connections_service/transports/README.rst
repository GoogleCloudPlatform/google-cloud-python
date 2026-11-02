
transport inheritance structure
_______________________________

``AppConnectionsServiceTransport`` is the ABC for all transports.

- public child ``AppConnectionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AppConnectionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAppConnectionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AppConnectionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
