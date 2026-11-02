
transport inheritance structure
_______________________________

``FirestoreTransport`` is the ABC for all transports.

- public child ``FirestoreGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FirestoreGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFirestoreRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FirestoreRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
