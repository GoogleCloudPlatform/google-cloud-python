
transport inheritance structure
_______________________________

``EntityServiceTransport`` is the ABC for all transports.

- public child ``EntityServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EntityServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEntityServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EntityServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
