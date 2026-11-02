
transport inheritance structure
_______________________________

``ClientGatewaysServiceTransport`` is the ABC for all transports.

- public child ``ClientGatewaysServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ClientGatewaysServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseClientGatewaysServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ClientGatewaysServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
