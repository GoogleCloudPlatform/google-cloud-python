
transport inheritance structure
_______________________________

``LicenseManagementServiceTransport`` is the ABC for all transports.

- public child ``LicenseManagementServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LicenseManagementServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLicenseManagementServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LicenseManagementServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
