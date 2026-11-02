
transport inheritance structure
_______________________________

``QuotaAdjusterSettingsManagerTransport`` is the ABC for all transports.

- public child ``QuotaAdjusterSettingsManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``QuotaAdjusterSettingsManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseQuotaAdjusterSettingsManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``QuotaAdjusterSettingsManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
