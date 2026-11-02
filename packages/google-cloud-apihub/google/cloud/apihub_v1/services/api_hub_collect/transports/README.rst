
transport inheritance structure
_______________________________

``ApiHubCollectTransport`` is the ABC for all transports.

- public child ``ApiHubCollectGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiHubCollectGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiHubCollectRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiHubCollectRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
