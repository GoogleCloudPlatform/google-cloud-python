
transport inheritance structure
_______________________________

``TripServiceTransport`` is the ABC for all transports.

- public child ``TripServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TripServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTripServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TripServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
