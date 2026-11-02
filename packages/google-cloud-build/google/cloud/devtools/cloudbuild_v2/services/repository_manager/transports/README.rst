
transport inheritance structure
_______________________________

``RepositoryManagerTransport`` is the ABC for all transports.

- public child ``RepositoryManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RepositoryManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRepositoryManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RepositoryManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
