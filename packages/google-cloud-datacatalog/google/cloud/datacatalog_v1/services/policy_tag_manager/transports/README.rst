
transport inheritance structure
_______________________________

``PolicyTagManagerTransport`` is the ABC for all transports.

- public child ``PolicyTagManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PolicyTagManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePolicyTagManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PolicyTagManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
