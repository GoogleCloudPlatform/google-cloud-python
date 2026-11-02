
transport inheritance structure
_______________________________

``GeneratorsTransport`` is the ABC for all transports.

- public child ``GeneratorsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GeneratorsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGeneratorsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GeneratorsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
