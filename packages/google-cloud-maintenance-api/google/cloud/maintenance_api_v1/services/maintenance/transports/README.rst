
transport inheritance structure
_______________________________

``MaintenanceTransport`` is the ABC for all transports.

- public child ``MaintenanceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MaintenanceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMaintenanceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MaintenanceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
