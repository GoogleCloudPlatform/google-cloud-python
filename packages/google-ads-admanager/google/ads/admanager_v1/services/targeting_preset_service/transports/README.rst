
transport inheritance structure
_______________________________

``TargetingPresetServiceTransport`` is the ABC for all transports.

- public child ``TargetingPresetServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TargetingPresetServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTargetingPresetServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TargetingPresetServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
