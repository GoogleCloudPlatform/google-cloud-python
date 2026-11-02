
transport inheritance structure
_______________________________

``GlobalNetworkEndpointGroupsTransport`` is the ABC for all transports.

- public child ``GlobalNetworkEndpointGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalNetworkEndpointGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalNetworkEndpointGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalNetworkEndpointGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
