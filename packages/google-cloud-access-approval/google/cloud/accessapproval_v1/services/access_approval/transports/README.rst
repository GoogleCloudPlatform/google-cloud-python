
transport inheritance structure
_______________________________

``AccessApprovalTransport`` is the ABC for all transports.

- public child ``AccessApprovalGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AccessApprovalGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAccessApprovalRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AccessApprovalRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
