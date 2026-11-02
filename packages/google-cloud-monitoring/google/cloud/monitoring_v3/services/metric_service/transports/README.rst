
transport inheritance structure
_______________________________

``MetricServiceTransport`` is the ABC for all transports.

- public child ``MetricServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MetricServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMetricServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MetricServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
