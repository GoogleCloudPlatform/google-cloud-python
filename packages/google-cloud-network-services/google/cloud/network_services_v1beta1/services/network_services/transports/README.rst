
transport inheritance structure
_______________________________

``NetworkServicesTransport`` is the ABC for all transports.

- public child ``NetworkServicesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkServicesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkServicesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkServicesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
