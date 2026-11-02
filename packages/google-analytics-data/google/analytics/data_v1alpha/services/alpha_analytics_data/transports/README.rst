
transport inheritance structure
_______________________________

``AlphaAnalyticsDataTransport`` is the ABC for all transports.

- public child ``AlphaAnalyticsDataGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AlphaAnalyticsDataGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAlphaAnalyticsDataRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AlphaAnalyticsDataRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
