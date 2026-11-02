
transport inheritance structure
_______________________________

``ClientConnectorServicesServiceTransport`` is the ABC for all transports.

- public child ``ClientConnectorServicesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ClientConnectorServicesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseClientConnectorServicesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ClientConnectorServicesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
