
transport inheritance structure
_______________________________

``IdentityMappingStoreServiceTransport`` is the ABC for all transports.

- public child ``IdentityMappingStoreServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IdentityMappingStoreServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIdentityMappingStoreServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IdentityMappingStoreServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
