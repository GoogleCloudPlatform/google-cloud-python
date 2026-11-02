
transport inheritance structure
_______________________________

``GlobalForwardingRulesTransport`` is the ABC for all transports.

- public child ``GlobalForwardingRulesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalForwardingRulesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalForwardingRulesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalForwardingRulesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
