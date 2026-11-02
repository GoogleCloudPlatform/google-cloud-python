
transport inheritance structure
_______________________________

``SqlFlagsServiceTransport`` is the ABC for all transports.

- public child ``SqlFlagsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlFlagsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlFlagsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlFlagsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
