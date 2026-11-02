
transport inheritance structure
_______________________________

``DataformTransport`` is the ABC for all transports.

- public child ``DataformGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataformGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataformRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataformRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
