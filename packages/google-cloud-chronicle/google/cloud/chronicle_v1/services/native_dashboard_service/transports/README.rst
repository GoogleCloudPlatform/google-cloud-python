
transport inheritance structure
_______________________________

``NativeDashboardServiceTransport`` is the ABC for all transports.

- public child ``NativeDashboardServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NativeDashboardServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNativeDashboardServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NativeDashboardServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
