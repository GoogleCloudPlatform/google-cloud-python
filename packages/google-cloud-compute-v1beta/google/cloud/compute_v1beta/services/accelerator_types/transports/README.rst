
transport inheritance structure
_______________________________

``AcceleratorTypesTransport`` is the ABC for all transports.

- public child ``AcceleratorTypesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AcceleratorTypesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAcceleratorTypesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AcceleratorTypesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
