
transport inheritance structure
_______________________________

``CustomTargetingKeyServiceTransport`` is the ABC for all transports.

- public child ``CustomTargetingKeyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CustomTargetingKeyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCustomTargetingKeyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CustomTargetingKeyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
