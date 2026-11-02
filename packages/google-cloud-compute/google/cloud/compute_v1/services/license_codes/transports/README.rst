
transport inheritance structure
_______________________________

``LicenseCodesTransport`` is the ABC for all transports.

- public child ``LicenseCodesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LicenseCodesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLicenseCodesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LicenseCodesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
