
transport inheritance structure
_______________________________

``NetworkEndpointGroupsTransport`` is the ABC for all transports.

- public child ``NetworkEndpointGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkEndpointGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkEndpointGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkEndpointGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
