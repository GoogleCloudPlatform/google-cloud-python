
transport inheritance structure
_______________________________

``MerchantReviewsServiceTransport`` is the ABC for all transports.

- public child ``MerchantReviewsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MerchantReviewsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMerchantReviewsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MerchantReviewsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
