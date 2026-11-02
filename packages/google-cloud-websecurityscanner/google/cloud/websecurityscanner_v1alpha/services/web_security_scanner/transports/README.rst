
transport inheritance structure
_______________________________

``WebSecurityScannerTransport`` is the ABC for all transports.

- public child ``WebSecurityScannerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WebSecurityScannerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWebSecurityScannerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WebSecurityScannerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
