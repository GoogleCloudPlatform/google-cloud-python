
transport inheritance structure
_______________________________

``CmsMetadataKeyServiceTransport`` is the ABC for all transports.

- public child ``CmsMetadataKeyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CmsMetadataKeyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCmsMetadataKeyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CmsMetadataKeyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
