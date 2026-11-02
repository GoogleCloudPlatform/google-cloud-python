
transport inheritance structure
_______________________________

``ArtifactRegistryTransport`` is the ABC for all transports.

- public child ``ArtifactRegistryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ArtifactRegistryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseArtifactRegistryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ArtifactRegistryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
