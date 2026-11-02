
transport inheritance structure
_______________________________

``InsightsConfigServiceTransport`` is the ABC for all transports.

- public child ``InsightsConfigServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InsightsConfigServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInsightsConfigServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InsightsConfigServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
