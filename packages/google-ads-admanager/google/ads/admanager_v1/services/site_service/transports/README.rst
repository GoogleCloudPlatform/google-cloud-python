
transport inheritance structure
_______________________________

``SiteServiceTransport`` is the ABC for all transports.

- public child ``SiteServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SiteServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSiteServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SiteServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
