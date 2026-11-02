
transport inheritance structure
_______________________________

``OracleDatabaseTransport`` is the ABC for all transports.

- public child ``OracleDatabaseGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OracleDatabaseGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOracleDatabaseRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OracleDatabaseRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
