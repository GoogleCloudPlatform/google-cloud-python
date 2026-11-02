
transport inheritance structure
_______________________________

``DataFusionTransport`` is the ABC for all transports.

- public child ``DataFusionGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataFusionGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataFusionRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataFusionRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
