
transport inheritance structure
_______________________________

``DatastoreAdminTransport`` is the ABC for all transports.

- public child ``DatastoreAdminGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DatastoreAdminGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDatastoreAdminRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DatastoreAdminRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
