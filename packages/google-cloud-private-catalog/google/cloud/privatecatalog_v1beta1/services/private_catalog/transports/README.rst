
transport inheritance structure
_______________________________

``PrivateCatalogTransport`` is the ABC for all transports.

- public child ``PrivateCatalogGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PrivateCatalogGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePrivateCatalogRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PrivateCatalogRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
