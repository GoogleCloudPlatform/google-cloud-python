
transport inheritance structure
_______________________________

``DiscussServiceTransport`` is the ABC for all transports.

- public child ``DiscussServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DiscussServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDiscussServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DiscussServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
