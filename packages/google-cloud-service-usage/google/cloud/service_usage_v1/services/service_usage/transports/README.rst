
transport inheritance structure
_______________________________

``ServiceUsageTransport`` is the ABC for all transports.

- public child ``ServiceUsageGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ServiceUsageGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseServiceUsageRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ServiceUsageRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
