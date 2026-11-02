
transport inheritance structure
_______________________________

``GatewayControlTransport`` is the ABC for all transports.

- public child ``GatewayControlGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GatewayControlGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGatewayControlRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GatewayControlRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
