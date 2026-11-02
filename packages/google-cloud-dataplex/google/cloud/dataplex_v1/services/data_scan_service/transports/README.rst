
transport inheritance structure
_______________________________

``DataScanServiceTransport`` is the ABC for all transports.

- public child ``DataScanServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataScanServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataScanServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataScanServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
