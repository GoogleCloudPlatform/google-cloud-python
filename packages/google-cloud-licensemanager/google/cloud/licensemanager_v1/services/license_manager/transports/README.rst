
transport inheritance structure
_______________________________

``LicenseManagerTransport`` is the ABC for all transports.

- public child ``LicenseManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LicenseManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLicenseManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LicenseManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
