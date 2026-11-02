
transport inheritance structure
_______________________________

``DeveloperKnowledgeTransport`` is the ABC for all transports.

- public child ``DeveloperKnowledgeGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DeveloperKnowledgeGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDeveloperKnowledgeRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DeveloperKnowledgeRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
