
transport inheritance structure
_______________________________

``EdgeNetworkTransport`` is the ABC for all transports.

- public child ``EdgeNetworkGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EdgeNetworkGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEdgeNetworkRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EdgeNetworkRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
