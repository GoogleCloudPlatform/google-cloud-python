
transport inheritance structure
_______________________________

``OrgPolicyTransport`` is the ABC for all transports.

- public child ``OrgPolicyGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrgPolicyGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrgPolicyRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrgPolicyRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
