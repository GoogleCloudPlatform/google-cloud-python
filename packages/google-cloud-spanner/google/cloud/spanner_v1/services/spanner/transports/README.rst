
transport inheritance structure
_______________________________

``SpannerTransport`` is the ABC for all transports.

- public child ``SpannerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SpannerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSpannerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SpannerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
