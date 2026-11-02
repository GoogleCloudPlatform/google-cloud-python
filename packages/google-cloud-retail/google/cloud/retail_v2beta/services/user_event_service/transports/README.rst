
transport inheritance structure
_______________________________

``UserEventServiceTransport`` is the ABC for all transports.

- public child ``UserEventServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UserEventServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUserEventServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UserEventServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
