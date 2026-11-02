
transport inheritance structure
_______________________________

``NodeTypesTransport`` is the ABC for all transports.

- public child ``NodeTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NodeTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNodeTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NodeTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
