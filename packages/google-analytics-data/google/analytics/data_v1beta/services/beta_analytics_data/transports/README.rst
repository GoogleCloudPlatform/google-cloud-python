
transport inheritance structure
_______________________________

``BetaAnalyticsDataTransport`` is the ABC for all transports.

- public child ``BetaAnalyticsDataGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BetaAnalyticsDataGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBetaAnalyticsDataRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BetaAnalyticsDataRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
