
transport inheritance structure
_______________________________

``RecommenderTransport`` is the ABC for all transports.

- public child ``RecommenderGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RecommenderGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRecommenderRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RecommenderRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
