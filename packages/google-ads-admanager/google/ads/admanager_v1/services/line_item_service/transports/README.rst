
transport inheritance structure
_______________________________

``LineItemServiceTransport`` is the ABC for all transports.

- public child ``LineItemServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LineItemServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLineItemServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LineItemServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
