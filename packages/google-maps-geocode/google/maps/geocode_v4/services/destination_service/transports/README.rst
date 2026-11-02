
transport inheritance structure
_______________________________

``DestinationServiceTransport`` is the ABC for all transports.

- public child ``DestinationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DestinationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDestinationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DestinationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
