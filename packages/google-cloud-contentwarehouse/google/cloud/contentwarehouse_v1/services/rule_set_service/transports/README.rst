
transport inheritance structure
_______________________________

``RuleSetServiceTransport`` is the ABC for all transports.

- public child ``RuleSetServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RuleSetServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRuleSetServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RuleSetServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
