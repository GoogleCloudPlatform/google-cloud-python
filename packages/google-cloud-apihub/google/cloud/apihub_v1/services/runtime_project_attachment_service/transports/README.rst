
transport inheritance structure
_______________________________

``RuntimeProjectAttachmentServiceTransport`` is the ABC for all transports.

- public child ``RuntimeProjectAttachmentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RuntimeProjectAttachmentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRuntimeProjectAttachmentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RuntimeProjectAttachmentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
