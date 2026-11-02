
transport inheritance structure
_______________________________

``ImageVersionsTransport`` is the ABC for all transports.

- public child ``ImageVersionsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ImageVersionsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseImageVersionsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ImageVersionsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
