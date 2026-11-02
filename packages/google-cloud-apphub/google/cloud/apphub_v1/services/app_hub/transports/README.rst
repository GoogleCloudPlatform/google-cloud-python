
transport inheritance structure
_______________________________

``AppHubTransport`` is the ABC for all transports.

- public child ``AppHubGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AppHubGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAppHubRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AppHubRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
