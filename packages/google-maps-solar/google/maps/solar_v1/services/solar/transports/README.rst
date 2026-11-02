
transport inheritance structure
_______________________________

``SolarTransport`` is the ABC for all transports.

- public child ``SolarGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SolarGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSolarRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SolarRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
