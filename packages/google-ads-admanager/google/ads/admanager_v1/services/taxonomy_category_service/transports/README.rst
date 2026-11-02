
transport inheritance structure
_______________________________

``TaxonomyCategoryServiceTransport`` is the ABC for all transports.

- public child ``TaxonomyCategoryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TaxonomyCategoryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTaxonomyCategoryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TaxonomyCategoryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
