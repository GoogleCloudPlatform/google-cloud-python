
transport inheritance structure
_______________________________

``OnlineReturnPolicyServiceTransport`` is the ABC for all transports.

- public child ``OnlineReturnPolicyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OnlineReturnPolicyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOnlineReturnPolicyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OnlineReturnPolicyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
