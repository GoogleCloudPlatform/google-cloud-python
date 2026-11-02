
transport inheritance structure
_______________________________

``UserListDirectLicenseServiceTransport`` is the ABC for all transports.

- public child ``UserListDirectLicenseServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UserListDirectLicenseServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUserListDirectLicenseServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UserListDirectLicenseServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
