
transport inheritance structure
_______________________________

``SqlTiersServiceTransport`` is the ABC for all transports.

- public child ``SqlTiersServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlTiersServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlTiersServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlTiersServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
