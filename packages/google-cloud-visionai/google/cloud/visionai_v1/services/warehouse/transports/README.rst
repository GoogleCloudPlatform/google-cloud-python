
transport inheritance structure
_______________________________

``WarehouseTransport`` is the ABC for all transports.

- public child ``WarehouseGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WarehouseGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWarehouseRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WarehouseRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
