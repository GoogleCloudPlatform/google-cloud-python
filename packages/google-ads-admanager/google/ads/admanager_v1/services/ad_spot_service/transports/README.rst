
transport inheritance structure
_______________________________

``AdSpotServiceTransport`` is the ABC for all transports.

- public child ``AdSpotServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AdSpotServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAdSpotServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AdSpotServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
