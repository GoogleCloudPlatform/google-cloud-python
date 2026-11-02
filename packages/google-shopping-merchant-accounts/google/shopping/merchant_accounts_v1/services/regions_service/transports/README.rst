
transport inheritance structure
_______________________________

``RegionsServiceTransport`` is the ABC for all transports.

- public child ``RegionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
