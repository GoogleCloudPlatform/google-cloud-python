
transport inheritance structure
_______________________________

``StreamingVideoIntelligenceServiceTransport`` is the ABC for all transports.

- public child ``StreamingVideoIntelligenceServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StreamingVideoIntelligenceServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStreamingVideoIntelligenceServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StreamingVideoIntelligenceServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
