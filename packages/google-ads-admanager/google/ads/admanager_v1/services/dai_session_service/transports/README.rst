
transport inheritance structure
_______________________________

``DaiSessionServiceTransport`` is the ABC for all transports.

- public child ``DaiSessionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DaiSessionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDaiSessionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DaiSessionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
