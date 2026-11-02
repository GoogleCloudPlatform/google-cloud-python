
transport inheritance structure
_______________________________

``BatchServiceTransport`` is the ABC for all transports.

- public child ``BatchServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BatchServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBatchServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BatchServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
