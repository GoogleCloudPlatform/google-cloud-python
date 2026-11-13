
transport inheritance structure
_______________________________

``YieldPartnerServiceTransport`` is the ABC for all transports.

- public child ``YieldPartnerServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``YieldPartnerServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseYieldPartnerServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``YieldPartnerServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
