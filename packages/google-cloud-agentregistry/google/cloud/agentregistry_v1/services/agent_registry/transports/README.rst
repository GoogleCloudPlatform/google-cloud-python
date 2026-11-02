
transport inheritance structure
_______________________________

``AgentRegistryTransport`` is the ABC for all transports.

- public child ``AgentRegistryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AgentRegistryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAgentRegistryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AgentRegistryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
