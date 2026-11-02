
transport inheritance structure
_______________________________

``WorkloadIdentityTransport`` is the ABC for all transports.

- public child ``WorkloadIdentityGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WorkloadIdentityGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWorkloadIdentityRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WorkloadIdentityRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
