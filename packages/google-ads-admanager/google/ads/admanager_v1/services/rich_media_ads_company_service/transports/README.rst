
transport inheritance structure
_______________________________

``RichMediaAdsCompanyServiceTransport`` is the ABC for all transports.

- public child ``RichMediaAdsCompanyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RichMediaAdsCompanyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRichMediaAdsCompanyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RichMediaAdsCompanyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
