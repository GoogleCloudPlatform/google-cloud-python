
transport inheritance structure
_______________________________

``VideoStitcherServiceTransport`` is the ABC for all transports.

- public child ``VideoStitcherServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VideoStitcherServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVideoStitcherServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VideoStitcherServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
