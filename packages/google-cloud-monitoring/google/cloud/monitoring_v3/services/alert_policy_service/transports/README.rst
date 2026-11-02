
transport inheritance structure
_______________________________

``AlertPolicyServiceTransport`` is the ABC for all transports.

- public child ``AlertPolicyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AlertPolicyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAlertPolicyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AlertPolicyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
