
transport inheritance structure
_______________________________

``CdnConfigServiceTransport`` is the ABC for all transports.

- public child ``CdnConfigServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CdnConfigServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCdnConfigServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CdnConfigServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
