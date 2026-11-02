
transport inheritance structure
_______________________________

``SecurityPoliciesTransport`` is the ABC for all transports.

- public child ``SecurityPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SecurityPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSecurityPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SecurityPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
