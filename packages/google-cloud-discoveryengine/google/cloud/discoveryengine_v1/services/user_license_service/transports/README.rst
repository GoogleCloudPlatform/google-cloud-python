
transport inheritance structure
_______________________________

``UserLicenseServiceTransport`` is the ABC for all transports.

- public child ``UserLicenseServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UserLicenseServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUserLicenseServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UserLicenseServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
