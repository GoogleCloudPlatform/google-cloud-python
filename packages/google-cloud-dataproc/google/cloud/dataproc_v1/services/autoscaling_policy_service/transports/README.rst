
transport inheritance structure
_______________________________

``AutoscalingPolicyServiceTransport`` is the ABC for all transports.

- public child ``AutoscalingPolicyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AutoscalingPolicyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAutoscalingPolicyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AutoscalingPolicyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
