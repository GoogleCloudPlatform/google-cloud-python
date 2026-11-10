
transport inheritance structure
_______________________________

``YieldGroupServiceTransport`` is the ABC for all transports.

- public child ``YieldGroupServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``YieldGroupServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseYieldGroupServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``YieldGroupServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
