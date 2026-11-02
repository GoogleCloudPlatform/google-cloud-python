
transport inheritance structure
_______________________________

``ClusterManagerTransport`` is the ABC for all transports.

- public child ``ClusterManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ClusterManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseClusterManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ClusterManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
