
transport inheritance structure
_______________________________

``SessionEntityTypesTransport`` is the ABC for all transports.

- public child ``SessionEntityTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SessionEntityTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSessionEntityTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SessionEntityTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
