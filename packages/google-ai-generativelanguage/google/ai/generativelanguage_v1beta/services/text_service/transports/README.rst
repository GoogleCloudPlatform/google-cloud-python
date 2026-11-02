
transport inheritance structure
_______________________________

``TextServiceTransport`` is the ABC for all transports.

- public child ``TextServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TextServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTextServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TextServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
