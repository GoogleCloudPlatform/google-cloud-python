
transport inheritance structure
_______________________________

``SearchTuningServiceTransport`` is the ABC for all transports.

- public child ``SearchTuningServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SearchTuningServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSearchTuningServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SearchTuningServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
