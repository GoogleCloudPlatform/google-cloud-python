
transport inheritance structure
_______________________________

``SqlAvailableDatabaseVersionsServiceTransport`` is the ABC for all transports.

- public child ``SqlAvailableDatabaseVersionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlAvailableDatabaseVersionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlAvailableDatabaseVersionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlAvailableDatabaseVersionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
