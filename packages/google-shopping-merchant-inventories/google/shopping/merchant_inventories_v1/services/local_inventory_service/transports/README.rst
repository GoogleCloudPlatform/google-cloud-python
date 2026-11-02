
transport inheritance structure
_______________________________

``LocalInventoryServiceTransport`` is the ABC for all transports.

- public child ``LocalInventoryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LocalInventoryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLocalInventoryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LocalInventoryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
