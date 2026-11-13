
transport inheritance structure
_______________________________

``SqlSslCertsServiceTransport`` is the ABC for all transports.

- public child ``SqlSslCertsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlSslCertsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlSslCertsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlSslCertsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
