
transport inheritance structure
_______________________________

``OsConfigServiceTransport`` is the ABC for all transports.

- public child ``OsConfigServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OsConfigServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOsConfigServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OsConfigServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
