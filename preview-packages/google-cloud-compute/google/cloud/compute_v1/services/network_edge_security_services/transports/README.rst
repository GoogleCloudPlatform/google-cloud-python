
transport inheritance structure
_______________________________

``NetworkEdgeSecurityServicesTransport`` is the ABC for all transports.

- public child ``NetworkEdgeSecurityServicesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkEdgeSecurityServicesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkEdgeSecurityServicesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkEdgeSecurityServicesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
