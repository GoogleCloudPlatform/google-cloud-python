
transport inheritance structure
_______________________________

``VersionsTransport`` is the ABC for all transports.

- public child ``VersionsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VersionsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVersionsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VersionsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
