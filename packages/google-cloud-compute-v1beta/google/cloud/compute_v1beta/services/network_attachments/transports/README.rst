
transport inheritance structure
_______________________________

``NetworkAttachmentsTransport`` is the ABC for all transports.

- public child ``NetworkAttachmentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkAttachmentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkAttachmentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkAttachmentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
