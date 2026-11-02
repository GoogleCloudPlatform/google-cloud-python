
transport inheritance structure
_______________________________

``CacheServiceTransport`` is the ABC for all transports.

- public child ``CacheServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CacheServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCacheServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CacheServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
