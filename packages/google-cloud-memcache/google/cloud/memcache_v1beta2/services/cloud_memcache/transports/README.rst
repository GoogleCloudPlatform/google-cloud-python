
transport inheritance structure
_______________________________

``CloudMemcacheTransport`` is the ABC for all transports.

- public child ``CloudMemcacheGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudMemcacheGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudMemcacheRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudMemcacheRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
