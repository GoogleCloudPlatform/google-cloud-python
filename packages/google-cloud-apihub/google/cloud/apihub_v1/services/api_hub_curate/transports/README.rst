
transport inheritance structure
_______________________________

``ApiHubCurateTransport`` is the ABC for all transports.

- public child ``ApiHubCurateGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiHubCurateGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiHubCurateRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiHubCurateRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
