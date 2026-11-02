
transport inheritance structure
_______________________________

``ApplicationServiceTransport`` is the ABC for all transports.

- public child ``ApplicationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApplicationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApplicationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApplicationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
