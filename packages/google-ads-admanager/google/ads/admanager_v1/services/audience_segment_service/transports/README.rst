
transport inheritance structure
_______________________________

``AudienceSegmentServiceTransport`` is the ABC for all transports.

- public child ``AudienceSegmentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AudienceSegmentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAudienceSegmentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AudienceSegmentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
