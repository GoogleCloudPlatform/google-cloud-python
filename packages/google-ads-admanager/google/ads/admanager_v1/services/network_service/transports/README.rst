
transport inheritance structure
_______________________________

``NetworkServiceTransport`` is the ABC for all transports.

- public child ``NetworkServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
