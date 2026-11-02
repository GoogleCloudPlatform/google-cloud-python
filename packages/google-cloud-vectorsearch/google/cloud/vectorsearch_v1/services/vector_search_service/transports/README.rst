
transport inheritance structure
_______________________________

``VectorSearchServiceTransport`` is the ABC for all transports.

- public child ``VectorSearchServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VectorSearchServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVectorSearchServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VectorSearchServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
