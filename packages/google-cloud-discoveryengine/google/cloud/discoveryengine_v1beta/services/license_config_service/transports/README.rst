
transport inheritance structure
_______________________________

``LicenseConfigServiceTransport`` is the ABC for all transports.

- public child ``LicenseConfigServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LicenseConfigServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLicenseConfigServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LicenseConfigServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
