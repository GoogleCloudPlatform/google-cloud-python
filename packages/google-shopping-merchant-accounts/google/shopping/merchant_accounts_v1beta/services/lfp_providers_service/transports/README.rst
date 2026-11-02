
transport inheritance structure
_______________________________

``LfpProvidersServiceTransport`` is the ABC for all transports.

- public child ``LfpProvidersServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LfpProvidersServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLfpProvidersServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LfpProvidersServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
