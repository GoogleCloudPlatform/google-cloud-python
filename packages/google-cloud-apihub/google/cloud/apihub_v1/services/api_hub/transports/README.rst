
transport inheritance structure
_______________________________

``ApiHubTransport`` is the ABC for all transports.

- public child ``ApiHubGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiHubGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiHubRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiHubRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
