
transport inheritance structure
_______________________________

``OmnichannelSettingsServiceTransport`` is the ABC for all transports.

- public child ``OmnichannelSettingsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OmnichannelSettingsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOmnichannelSettingsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OmnichannelSettingsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
