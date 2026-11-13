
transport inheritance structure
_______________________________

``AcceleratorInterconnectsTransport`` is the ABC for all transports.

- public child ``AcceleratorInterconnectsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AcceleratorInterconnectsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAcceleratorInterconnectsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AcceleratorInterconnectsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
