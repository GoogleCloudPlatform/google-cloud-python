
transport inheritance structure
_______________________________

``ProductReviewsServiceTransport`` is the ABC for all transports.

- public child ``ProductReviewsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ProductReviewsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseProductReviewsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ProductReviewsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
