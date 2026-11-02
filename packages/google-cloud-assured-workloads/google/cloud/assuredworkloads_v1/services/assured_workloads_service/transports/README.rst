
transport inheritance structure
_______________________________

``AssuredWorkloadsServiceTransport`` is the ABC for all transports.

- public child ``AssuredWorkloadsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AssuredWorkloadsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAssuredWorkloadsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AssuredWorkloadsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
