
transport inheritance structure
_______________________________

``WireGroupsTransport`` is the ABC for all transports.

- public child ``WireGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WireGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWireGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WireGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
