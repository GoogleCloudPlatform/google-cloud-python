
transport inheritance structure
_______________________________

``CloudProductRegistryReadServiceTransport`` is the ABC for all transports.

- public child ``CloudProductRegistryReadServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudProductRegistryReadServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudProductRegistryReadServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudProductRegistryReadServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
