
transport inheritance structure
_______________________________

``LineageTransport`` is the ABC for all transports.

- public child ``LineageGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LineageGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLineageRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LineageRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
