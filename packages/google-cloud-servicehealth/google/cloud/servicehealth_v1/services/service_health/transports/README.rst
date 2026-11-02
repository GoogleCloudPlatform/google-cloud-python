
transport inheritance structure
_______________________________

``ServiceHealthTransport`` is the ABC for all transports.

- public child ``ServiceHealthGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ServiceHealthGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseServiceHealthRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ServiceHealthRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
