
transport inheritance structure
_______________________________

``RecommendationServiceTransport`` is the ABC for all transports.

- public child ``RecommendationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RecommendationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRecommendationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RecommendationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
