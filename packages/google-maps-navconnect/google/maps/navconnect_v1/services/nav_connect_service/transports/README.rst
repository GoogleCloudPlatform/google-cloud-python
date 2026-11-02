
transport inheritance structure
_______________________________

``NavConnectServiceTransport`` is the ABC for all transports.

- public child ``NavConnectServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NavConnectServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNavConnectServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NavConnectServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
