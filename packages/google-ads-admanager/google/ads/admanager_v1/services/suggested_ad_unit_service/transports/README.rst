
transport inheritance structure
_______________________________

``SuggestedAdUnitServiceTransport`` is the ABC for all transports.

- public child ``SuggestedAdUnitServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SuggestedAdUnitServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSuggestedAdUnitServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SuggestedAdUnitServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
