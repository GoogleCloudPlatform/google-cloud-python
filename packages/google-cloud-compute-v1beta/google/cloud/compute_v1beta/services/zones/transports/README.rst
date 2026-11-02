
transport inheritance structure
_______________________________

``ZonesTransport`` is the ABC for all transports.

- public child ``ZonesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ZonesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseZonesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ZonesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
