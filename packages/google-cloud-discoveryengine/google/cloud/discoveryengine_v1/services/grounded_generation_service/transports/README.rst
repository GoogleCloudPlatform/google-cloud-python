
transport inheritance structure
_______________________________

``GroundedGenerationServiceTransport`` is the ABC for all transports.

- public child ``GroundedGenerationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GroundedGenerationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGroundedGenerationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GroundedGenerationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
