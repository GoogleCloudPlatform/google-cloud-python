
transport inheritance structure
_______________________________

``DiskTypesTransport`` is the ABC for all transports.

- public child ``DiskTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DiskTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDiskTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DiskTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
