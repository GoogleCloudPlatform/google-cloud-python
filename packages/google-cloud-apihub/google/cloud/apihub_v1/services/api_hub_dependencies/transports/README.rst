
transport inheritance structure
_______________________________

``ApiHubDependenciesTransport`` is the ABC for all transports.

- public child ``ApiHubDependenciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiHubDependenciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiHubDependenciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiHubDependenciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
