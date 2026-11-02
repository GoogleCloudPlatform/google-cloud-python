
transport inheritance structure
_______________________________

``CaseAttachmentServiceTransport`` is the ABC for all transports.

- public child ``CaseAttachmentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CaseAttachmentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCaseAttachmentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CaseAttachmentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
