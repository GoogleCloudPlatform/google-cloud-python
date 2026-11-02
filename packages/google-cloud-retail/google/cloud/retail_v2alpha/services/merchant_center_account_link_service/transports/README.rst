
transport inheritance structure
_______________________________

``MerchantCenterAccountLinkServiceTransport`` is the ABC for all transports.

- public child ``MerchantCenterAccountLinkServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MerchantCenterAccountLinkServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMerchantCenterAccountLinkServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MerchantCenterAccountLinkServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
