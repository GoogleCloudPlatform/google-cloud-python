
transport inheritance structure
_______________________________

``DocumentProcessorServiceTransport`` is the ABC for all transports.

- public child ``DocumentProcessorServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DocumentProcessorServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDocumentProcessorServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DocumentProcessorServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
