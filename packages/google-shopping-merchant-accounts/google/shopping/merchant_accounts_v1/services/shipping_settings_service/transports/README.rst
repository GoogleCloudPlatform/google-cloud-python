
transport inheritance structure
_______________________________

``ShippingSettingsServiceTransport`` is the ABC for all transports.

- public child ``ShippingSettingsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ShippingSettingsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseShippingSettingsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ShippingSettingsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
