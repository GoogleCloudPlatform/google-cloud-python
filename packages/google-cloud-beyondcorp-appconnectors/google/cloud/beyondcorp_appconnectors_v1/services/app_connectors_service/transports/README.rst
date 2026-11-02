
transport inheritance structure
_______________________________

``AppConnectorsServiceTransport`` is the ABC for all transports.

- public child ``AppConnectorsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AppConnectorsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAppConnectorsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AppConnectorsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
