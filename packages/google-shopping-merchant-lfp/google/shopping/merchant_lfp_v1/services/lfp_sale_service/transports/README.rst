
transport inheritance structure
_______________________________

``LfpSaleServiceTransport`` is the ABC for all transports.

- public child ``LfpSaleServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LfpSaleServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLfpSaleServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LfpSaleServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
