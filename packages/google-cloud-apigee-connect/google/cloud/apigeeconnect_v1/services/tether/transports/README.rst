
transport inheritance structure
_______________________________

``TetherTransport`` is the ABC for all transports.

- public child ``TetherGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TetherGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTetherRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TetherRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
