
transport inheritance structure
_______________________________

``HealthChecksTransport`` is the ABC for all transports.

- public child ``HealthChecksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HealthChecksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHealthChecksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HealthChecksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
