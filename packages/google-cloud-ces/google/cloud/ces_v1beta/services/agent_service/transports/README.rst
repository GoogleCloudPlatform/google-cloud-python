
transport inheritance structure
_______________________________

``AgentServiceTransport`` is the ABC for all transports.

- public child ``AgentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AgentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAgentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AgentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
