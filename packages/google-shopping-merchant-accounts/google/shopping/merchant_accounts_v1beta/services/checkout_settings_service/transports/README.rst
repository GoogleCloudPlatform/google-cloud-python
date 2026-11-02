
transport inheritance structure
_______________________________

``CheckoutSettingsServiceTransport`` is the ABC for all transports.

- public child ``CheckoutSettingsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CheckoutSettingsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCheckoutSettingsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CheckoutSettingsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
