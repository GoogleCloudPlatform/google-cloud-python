
transport inheritance structure
_______________________________

``AdBreakServiceTransport`` is the ABC for all transports.

- public child ``AdBreakServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AdBreakServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAdBreakServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AdBreakServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
