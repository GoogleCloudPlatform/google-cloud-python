
transport inheritance structure
_______________________________

``ConnectionServiceTransport`` is the ABC for all transports.

- public child ``ConnectionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConnectionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConnectionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConnectionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
