
transport inheritance structure
_______________________________

``FileServiceTransport`` is the ABC for all transports.

- public child ``FileServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FileServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFileServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FileServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
