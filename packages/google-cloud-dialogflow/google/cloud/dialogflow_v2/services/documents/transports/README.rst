
transport inheritance structure
_______________________________

``DocumentsTransport`` is the ABC for all transports.

- public child ``DocumentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DocumentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDocumentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DocumentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
