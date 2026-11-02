
transport inheritance structure
_______________________________

``CatalogServiceTransport`` is the ABC for all transports.

- public child ``CatalogServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CatalogServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCatalogServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CatalogServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
