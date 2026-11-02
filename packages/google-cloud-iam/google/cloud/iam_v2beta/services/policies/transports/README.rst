
transport inheritance structure
_______________________________

``PoliciesTransport`` is the ABC for all transports.

- public child ``PoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
