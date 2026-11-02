
transport inheritance structure
_______________________________

``CloudCatalogTransport`` is the ABC for all transports.

- public child ``CloudCatalogGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudCatalogGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudCatalogRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudCatalogRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
