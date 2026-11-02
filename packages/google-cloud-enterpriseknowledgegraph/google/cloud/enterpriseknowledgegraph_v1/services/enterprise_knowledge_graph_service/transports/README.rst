
transport inheritance structure
_______________________________

``EnterpriseKnowledgeGraphServiceTransport`` is the ABC for all transports.

- public child ``EnterpriseKnowledgeGraphServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EnterpriseKnowledgeGraphServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEnterpriseKnowledgeGraphServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EnterpriseKnowledgeGraphServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
