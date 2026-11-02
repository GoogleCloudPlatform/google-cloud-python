
transport inheritance structure
_______________________________

``RolloutsTransport`` is the ABC for all transports.

- public child ``RolloutsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RolloutsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRolloutsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RolloutsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
