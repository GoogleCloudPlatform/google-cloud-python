
transport inheritance structure
_______________________________

``ManagedRulesetsTransport`` is the ABC for all transports.

- public child ``ManagedRulesetsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ManagedRulesetsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseManagedRulesetsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ManagedRulesetsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
