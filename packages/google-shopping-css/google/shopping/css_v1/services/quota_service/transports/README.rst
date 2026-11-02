
transport inheritance structure
_______________________________

``QuotaServiceTransport`` is the ABC for all transports.

- public child ``QuotaServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``QuotaServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseQuotaServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``QuotaServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
