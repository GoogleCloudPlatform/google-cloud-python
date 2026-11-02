
transport inheritance structure
_______________________________

``SqlRegionsServiceTransport`` is the ABC for all transports.

- public child ``SqlRegionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlRegionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlRegionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlRegionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
