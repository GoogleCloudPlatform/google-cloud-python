
transport inheritance structure
_______________________________

``AreaInsightsTransport`` is the ABC for all transports.

- public child ``AreaInsightsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AreaInsightsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAreaInsightsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AreaInsightsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
