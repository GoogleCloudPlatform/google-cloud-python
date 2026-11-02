
transport inheritance structure
_______________________________

``NodeGroupsTransport`` is the ABC for all transports.

- public child ``NodeGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NodeGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNodeGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NodeGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
