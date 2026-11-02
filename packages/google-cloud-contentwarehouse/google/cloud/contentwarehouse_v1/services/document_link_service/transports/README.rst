
transport inheritance structure
_______________________________

``DocumentLinkServiceTransport`` is the ABC for all transports.

- public child ``DocumentLinkServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DocumentLinkServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDocumentLinkServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DocumentLinkServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
