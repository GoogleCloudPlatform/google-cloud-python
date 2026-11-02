
transport inheritance structure
_______________________________

``ImageViewsTransport`` is the ABC for all transports.

- public child ``ImageViewsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ImageViewsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseImageViewsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ImageViewsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
