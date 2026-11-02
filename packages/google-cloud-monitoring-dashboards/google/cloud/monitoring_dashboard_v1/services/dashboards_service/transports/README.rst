
transport inheritance structure
_______________________________

``DashboardsServiceTransport`` is the ABC for all transports.

- public child ``DashboardsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DashboardsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDashboardsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DashboardsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
