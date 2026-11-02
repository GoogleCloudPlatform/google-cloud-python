
transport inheritance structure
_______________________________

``VehicleServiceTransport`` is the ABC for all transports.

- public child ``VehicleServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VehicleServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVehicleServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VehicleServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
