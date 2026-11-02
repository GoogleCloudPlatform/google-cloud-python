
transport inheritance structure
_______________________________

``EdgeContainerTransport`` is the ABC for all transports.

- public child ``EdgeContainerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EdgeContainerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEdgeContainerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EdgeContainerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
