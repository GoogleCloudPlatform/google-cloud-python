
transport inheritance structure
_______________________________

``SnoozeServiceTransport`` is the ABC for all transports.

- public child ``SnoozeServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SnoozeServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSnoozeServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SnoozeServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
