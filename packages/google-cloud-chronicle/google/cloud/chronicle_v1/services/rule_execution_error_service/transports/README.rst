
transport inheritance structure
_______________________________

``RuleExecutionErrorServiceTransport`` is the ABC for all transports.

- public child ``RuleExecutionErrorServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RuleExecutionErrorServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRuleExecutionErrorServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RuleExecutionErrorServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
