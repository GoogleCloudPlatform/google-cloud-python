
transport inheritance structure
_______________________________

``DataTaxonomyServiceTransport`` is the ABC for all transports.

- public child ``DataTaxonomyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataTaxonomyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataTaxonomyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataTaxonomyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
