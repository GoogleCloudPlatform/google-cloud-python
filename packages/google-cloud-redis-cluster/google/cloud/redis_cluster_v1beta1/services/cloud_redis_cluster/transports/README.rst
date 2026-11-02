
transport inheritance structure
_______________________________

``CloudRedisClusterTransport`` is the ABC for all transports.

- public child ``CloudRedisClusterGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudRedisClusterGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudRedisClusterRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudRedisClusterRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
