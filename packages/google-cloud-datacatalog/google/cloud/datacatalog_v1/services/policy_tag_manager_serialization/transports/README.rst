
transport inheritance structure
_______________________________

``PolicyTagManagerSerializationTransport`` is the ABC for all transports.

- public child ``PolicyTagManagerSerializationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PolicyTagManagerSerializationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePolicyTagManagerSerializationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PolicyTagManagerSerializationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
