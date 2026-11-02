
transport inheritance structure
_______________________________

``PrincipalAccessBoundaryPoliciesTransport`` is the ABC for all transports.

- public child ``PrincipalAccessBoundaryPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePrincipalAccessBoundaryPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PrincipalAccessBoundaryPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
