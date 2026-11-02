
transport inheritance structure
_______________________________

``RegionBackendBucketsTransport`` is the ABC for all transports.

- public child ``RegionBackendBucketsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionBackendBucketsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionBackendBucketsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionBackendBucketsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
