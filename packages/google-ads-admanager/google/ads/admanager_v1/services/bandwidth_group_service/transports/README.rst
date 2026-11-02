
transport inheritance structure
_______________________________

``BandwidthGroupServiceTransport`` is the ABC for all transports.

- public child ``BandwidthGroupServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BandwidthGroupServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBandwidthGroupServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BandwidthGroupServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
