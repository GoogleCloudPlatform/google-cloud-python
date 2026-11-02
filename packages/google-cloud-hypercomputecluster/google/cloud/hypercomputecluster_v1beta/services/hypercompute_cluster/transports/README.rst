
transport inheritance structure
_______________________________

``HypercomputeClusterTransport`` is the ABC for all transports.

- public child ``HypercomputeClusterGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HypercomputeClusterGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHypercomputeClusterRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HypercomputeClusterRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
