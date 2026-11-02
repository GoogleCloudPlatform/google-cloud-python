
transport inheritance structure
_______________________________

``AnalyticsHubServiceTransport`` is the ABC for all transports.

- public child ``AnalyticsHubServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AnalyticsHubServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAnalyticsHubServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AnalyticsHubServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
