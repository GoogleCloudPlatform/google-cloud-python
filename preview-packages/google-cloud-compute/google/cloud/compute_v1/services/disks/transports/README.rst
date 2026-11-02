
transport inheritance structure
_______________________________

``DisksTransport`` is the ABC for all transports.

- public child ``DisksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DisksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDisksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DisksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
