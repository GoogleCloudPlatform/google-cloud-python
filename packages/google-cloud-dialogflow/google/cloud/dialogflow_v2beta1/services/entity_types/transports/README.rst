
transport inheritance structure
_______________________________

``EntityTypesTransport`` is the ABC for all transports.

- public child ``EntityTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EntityTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEntityTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EntityTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
