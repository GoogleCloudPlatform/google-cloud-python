
transport inheritance structure
_______________________________

``FeaturedContentNativeDashboardServiceTransport`` is the ABC for all transports.

- public child ``FeaturedContentNativeDashboardServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FeaturedContentNativeDashboardServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFeaturedContentNativeDashboardServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FeaturedContentNativeDashboardServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
