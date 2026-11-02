
transport inheritance structure
_______________________________

``ReachabilityServiceTransport`` is the ABC for all transports.

- public child ``ReachabilityServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReachabilityServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReachabilityServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReachabilityServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
