
transport inheritance structure
_______________________________

``RouteOptimizationTransport`` is the ABC for all transports.

- public child ``RouteOptimizationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RouteOptimizationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRouteOptimizationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RouteOptimizationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
