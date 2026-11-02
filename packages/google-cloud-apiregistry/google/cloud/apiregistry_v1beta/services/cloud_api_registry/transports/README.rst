
transport inheritance structure
_______________________________

``CloudApiRegistryTransport`` is the ABC for all transports.

- public child ``CloudApiRegistryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudApiRegistryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudApiRegistryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudApiRegistryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
