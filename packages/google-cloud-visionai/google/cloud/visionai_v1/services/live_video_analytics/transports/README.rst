
transport inheritance structure
_______________________________

``LiveVideoAnalyticsTransport`` is the ABC for all transports.

- public child ``LiveVideoAnalyticsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LiveVideoAnalyticsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLiveVideoAnalyticsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LiveVideoAnalyticsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
