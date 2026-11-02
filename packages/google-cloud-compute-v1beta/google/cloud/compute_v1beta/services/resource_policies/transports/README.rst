
transport inheritance structure
_______________________________

``ResourcePoliciesTransport`` is the ABC for all transports.

- public child ``ResourcePoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ResourcePoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseResourcePoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ResourcePoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
