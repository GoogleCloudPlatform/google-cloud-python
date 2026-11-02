
transport inheritance structure
_______________________________

``ApiGatewayServiceTransport`` is the ABC for all transports.

- public child ``ApiGatewayServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiGatewayServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiGatewayServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiGatewayServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
