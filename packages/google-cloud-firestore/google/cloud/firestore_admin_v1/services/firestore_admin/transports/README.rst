
transport inheritance structure
_______________________________

``FirestoreAdminTransport`` is the ABC for all transports.

- public child ``FirestoreAdminGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FirestoreAdminGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFirestoreAdminRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FirestoreAdminRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
