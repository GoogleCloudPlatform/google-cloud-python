
transport inheritance structure
_______________________________

``DatastoreTransport`` is the ABC for all transports.

- public child ``DatastoreGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DatastoreGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDatastoreRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DatastoreRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
