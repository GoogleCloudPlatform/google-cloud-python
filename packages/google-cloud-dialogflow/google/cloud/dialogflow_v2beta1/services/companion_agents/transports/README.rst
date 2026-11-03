
transport inheritance structure
_______________________________

``CompanionAgentsTransport`` is the ABC for all transports.

- public child ``CompanionAgentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CompanionAgentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCompanionAgentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CompanionAgentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
