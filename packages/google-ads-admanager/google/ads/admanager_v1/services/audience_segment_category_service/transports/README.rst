
transport inheritance structure
_______________________________

``AudienceSegmentCategoryServiceTransport`` is the ABC for all transports.

- public child ``AudienceSegmentCategoryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AudienceSegmentCategoryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAudienceSegmentCategoryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AudienceSegmentCategoryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
