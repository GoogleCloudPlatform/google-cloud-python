
transport inheritance structure
_______________________________

``LivestreamServiceTransport`` is the ABC for all transports.

- public child ``LivestreamServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LivestreamServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLivestreamServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LivestreamServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
