
transport inheritance structure
_______________________________

``HealthCheckServiceTransport`` is the ABC for all transports.

- public child ``HealthCheckServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HealthCheckServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHealthCheckServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HealthCheckServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
