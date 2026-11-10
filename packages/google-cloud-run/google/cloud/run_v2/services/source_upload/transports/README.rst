
transport inheritance structure
_______________________________

``SourceUploadTransport`` is the ABC for all transports.

- public child ``SourceUploadGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SourceUploadGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSourceUploadRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SourceUploadRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
