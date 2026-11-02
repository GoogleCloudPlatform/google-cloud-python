
transport inheritance structure
_______________________________

``ClusterControllerTransport`` is the ABC for all transports.

- public child ``ClusterControllerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ClusterControllerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseClusterControllerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ClusterControllerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
