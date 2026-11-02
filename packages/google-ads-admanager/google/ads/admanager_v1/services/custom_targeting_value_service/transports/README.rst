
transport inheritance structure
_______________________________

``CustomTargetingValueServiceTransport`` is the ABC for all transports.

- public child ``CustomTargetingValueServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CustomTargetingValueServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCustomTargetingValueServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CustomTargetingValueServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
