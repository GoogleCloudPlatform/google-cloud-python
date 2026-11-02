
transport inheritance structure
_______________________________

``RuleServiceTransport`` is the ABC for all transports.

- public child ``RuleServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RuleServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRuleServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RuleServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
