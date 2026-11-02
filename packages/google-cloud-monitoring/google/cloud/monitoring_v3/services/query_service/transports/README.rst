
transport inheritance structure
_______________________________

``QueryServiceTransport`` is the ABC for all transports.

- public child ``QueryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``QueryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseQueryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``QueryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
