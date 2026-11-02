
transport inheritance structure
_______________________________

``SqlFeatureEligibilityServiceTransport`` is the ABC for all transports.

- public child ``SqlFeatureEligibilityServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SqlFeatureEligibilityServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSqlFeatureEligibilityServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SqlFeatureEligibilityServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
