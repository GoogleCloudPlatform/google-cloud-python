
transport inheritance structure
_______________________________

``AppTopologyTransport`` is the ABC for all transports.

- public child ``AppTopologyGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AppTopologyGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAppTopologyRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AppTopologyRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
