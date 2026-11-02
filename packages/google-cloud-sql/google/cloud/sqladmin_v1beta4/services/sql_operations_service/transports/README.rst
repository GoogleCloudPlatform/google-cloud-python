
transport inheritance structure
_______________________________

``SqlOperationsServiceTransport`` is the ABC for all transports.

- public child ``SqlOperationsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlOperationsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlOperationsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlOperationsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
