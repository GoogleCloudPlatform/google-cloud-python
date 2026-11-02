
transport inheritance structure
_______________________________

``LiveStreamServiceTransport`` is the ABC for all transports.

- public child ``LiveStreamServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LiveStreamServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLiveStreamServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LiveStreamServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
