
transport inheritance structure
_______________________________

``ImagesTransport`` is the ABC for all transports.

- public child ``ImagesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ImagesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseImagesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ImagesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
