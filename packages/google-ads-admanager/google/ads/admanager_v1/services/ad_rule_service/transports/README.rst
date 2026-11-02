
transport inheritance structure
_______________________________

``AdRuleServiceTransport`` is the ABC for all transports.

- public child ``AdRuleServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AdRuleServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAdRuleServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AdRuleServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
