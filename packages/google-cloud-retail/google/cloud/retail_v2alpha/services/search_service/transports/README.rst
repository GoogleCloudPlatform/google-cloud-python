
transport inheritance structure
_______________________________

``SearchServiceTransport`` is the ABC for all transports.

- public child ``SearchServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SearchServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSearchServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SearchServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
