
transport inheritance structure
_______________________________

``InterconnectAttachmentsTransport`` is the ABC for all transports.

- public child ``InterconnectAttachmentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InterconnectAttachmentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInterconnectAttachmentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InterconnectAttachmentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
