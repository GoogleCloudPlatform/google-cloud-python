
transport inheritance structure
_______________________________

``RegionNetworkEndpointGroupsTransport`` is the ABC for all transports.

- public child ``RegionNetworkEndpointGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionNetworkEndpointGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionNetworkEndpointGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionNetworkEndpointGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
