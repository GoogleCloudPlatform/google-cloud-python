
transport inheritance structure
_______________________________

``AdUnitServiceTransport`` is the ABC for all transports.

- public child ``AdUnitServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AdUnitServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAdUnitServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AdUnitServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
