
transport inheritance structure
_______________________________

``RevisionsTransport`` is the ABC for all transports.

- public child ``RevisionsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RevisionsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRevisionsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RevisionsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
