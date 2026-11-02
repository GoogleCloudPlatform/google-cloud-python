
transport inheritance structure
_______________________________

``ApiHubDiscoveryTransport`` is the ABC for all transports.

- public child ``ApiHubDiscoveryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiHubDiscoveryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiHubDiscoveryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiHubDiscoveryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
