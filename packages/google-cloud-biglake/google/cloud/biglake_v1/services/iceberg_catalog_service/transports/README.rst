
transport inheritance structure
_______________________________

``IcebergCatalogServiceTransport`` is the ABC for all transports.

- public child ``IcebergCatalogServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IcebergCatalogServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIcebergCatalogServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IcebergCatalogServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
