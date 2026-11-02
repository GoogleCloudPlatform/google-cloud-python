
transport inheritance structure
_______________________________

``AgentsTransport`` is the ABC for all transports.

- public child ``AgentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AgentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAgentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AgentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
