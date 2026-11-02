
transport inheritance structure
_______________________________

``ServiceAttachmentsTransport`` is the ABC for all transports.

- public child ``ServiceAttachmentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ServiceAttachmentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseServiceAttachmentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ServiceAttachmentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
