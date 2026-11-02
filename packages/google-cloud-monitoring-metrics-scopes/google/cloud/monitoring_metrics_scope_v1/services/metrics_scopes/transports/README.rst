
transport inheritance structure
_______________________________

``MetricsScopesTransport`` is the ABC for all transports.

- public child ``MetricsScopesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MetricsScopesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMetricsScopesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MetricsScopesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
