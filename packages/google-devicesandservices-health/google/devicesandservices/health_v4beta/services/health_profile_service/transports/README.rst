
transport inheritance structure
_______________________________

``HealthProfileServiceTransport`` is the ABC for all transports.

- public child ``HealthProfileServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HealthProfileServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHealthProfileServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HealthProfileServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
