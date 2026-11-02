
transport inheritance structure
_______________________________

``OrgPolicyViolationsPreviewServiceTransport`` is the ABC for all transports.

- public child ``OrgPolicyViolationsPreviewServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrgPolicyViolationsPreviewServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrgPolicyViolationsPreviewServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrgPolicyViolationsPreviewServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
