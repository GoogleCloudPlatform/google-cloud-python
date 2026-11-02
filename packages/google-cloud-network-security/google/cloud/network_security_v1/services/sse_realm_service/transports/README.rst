
transport inheritance structure
_______________________________

``SSERealmServiceTransport`` is the ABC for all transports.

- public child ``SSERealmServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SSERealmServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSSERealmServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SSERealmServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
