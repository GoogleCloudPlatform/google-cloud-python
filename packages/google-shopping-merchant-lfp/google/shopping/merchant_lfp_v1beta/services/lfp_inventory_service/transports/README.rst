
transport inheritance structure
_______________________________

``LfpInventoryServiceTransport`` is the ABC for all transports.

- public child ``LfpInventoryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LfpInventoryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLfpInventoryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LfpInventoryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
