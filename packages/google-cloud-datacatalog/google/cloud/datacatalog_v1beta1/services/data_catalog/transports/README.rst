
transport inheritance structure
_______________________________

``DataCatalogTransport`` is the ABC for all transports.

- public child ``DataCatalogGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataCatalogGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataCatalogRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataCatalogRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
