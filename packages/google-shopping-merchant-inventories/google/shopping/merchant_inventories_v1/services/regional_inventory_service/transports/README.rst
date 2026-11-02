
transport inheritance structure
_______________________________

``RegionalInventoryServiceTransport`` is the ABC for all transports.

- public child ``RegionalInventoryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionalInventoryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionalInventoryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionalInventoryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
