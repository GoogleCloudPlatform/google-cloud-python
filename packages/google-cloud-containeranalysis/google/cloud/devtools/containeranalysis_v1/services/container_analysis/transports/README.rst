
transport inheritance structure
_______________________________

``ContainerAnalysisTransport`` is the ABC for all transports.

- public child ``ContainerAnalysisGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ContainerAnalysisGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseContainerAnalysisRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ContainerAnalysisRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
