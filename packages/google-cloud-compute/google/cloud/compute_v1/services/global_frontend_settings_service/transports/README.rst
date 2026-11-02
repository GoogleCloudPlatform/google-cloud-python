
transport inheritance structure
_______________________________

``GlobalFrontendSettingsServiceTransport`` is the ABC for all transports.

- public child ``GlobalFrontendSettingsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalFrontendSettingsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalFrontendSettingsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalFrontendSettingsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
