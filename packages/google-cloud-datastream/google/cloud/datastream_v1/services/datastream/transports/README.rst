
transport inheritance structure
_______________________________

``DatastreamTransport`` is the ABC for all transports.

- public child ``DatastreamGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DatastreamGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDatastreamRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DatastreamRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
