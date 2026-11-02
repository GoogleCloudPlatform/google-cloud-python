
transport inheritance structure
_______________________________

``HubServiceTransport`` is the ABC for all transports.

- public child ``HubServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HubServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHubServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HubServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
