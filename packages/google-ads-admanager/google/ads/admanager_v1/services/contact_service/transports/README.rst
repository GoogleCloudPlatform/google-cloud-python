
transport inheritance structure
_______________________________

``ContactServiceTransport`` is the ABC for all transports.

- public child ``ContactServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ContactServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseContactServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ContactServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
