
transport inheritance structure
_______________________________

``ImageServiceTransport`` is the ABC for all transports.

- public child ``ImageServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ImageServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseImageServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ImageServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
