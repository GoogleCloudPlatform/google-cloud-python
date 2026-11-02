
transport inheritance structure
_______________________________

``AnalyticsAdminServiceTransport`` is the ABC for all transports.

- public child ``AnalyticsAdminServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AnalyticsAdminServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAnalyticsAdminServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AnalyticsAdminServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
