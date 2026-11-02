
transport inheritance structure
_______________________________

``OsConfigZonalServiceTransport`` is the ABC for all transports.

- public child ``OsConfigZonalServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OsConfigZonalServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOsConfigZonalServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OsConfigZonalServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
