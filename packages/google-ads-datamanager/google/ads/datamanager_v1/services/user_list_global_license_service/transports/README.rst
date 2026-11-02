
transport inheritance structure
_______________________________

``UserListGlobalLicenseServiceTransport`` is the ABC for all transports.

- public child ``UserListGlobalLicenseServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UserListGlobalLicenseServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUserListGlobalLicenseServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UserListGlobalLicenseServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
