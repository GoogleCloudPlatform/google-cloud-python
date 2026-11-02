
transport inheritance structure
_______________________________

``LfpStoreServiceTransport`` is the ABC for all transports.

- public child ``LfpStoreServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LfpStoreServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLfpStoreServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LfpStoreServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
