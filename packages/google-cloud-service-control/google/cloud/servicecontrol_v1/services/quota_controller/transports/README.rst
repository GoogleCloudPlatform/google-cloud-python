
transport inheritance structure
_______________________________

``QuotaControllerTransport`` is the ABC for all transports.

- public child ``QuotaControllerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``QuotaControllerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseQuotaControllerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``QuotaControllerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
