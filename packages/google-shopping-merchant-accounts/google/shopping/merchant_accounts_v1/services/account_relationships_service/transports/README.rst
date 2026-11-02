
transport inheritance structure
_______________________________

``AccountRelationshipsServiceTransport`` is the ABC for all transports.

- public child ``AccountRelationshipsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AccountRelationshipsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAccountRelationshipsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AccountRelationshipsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
