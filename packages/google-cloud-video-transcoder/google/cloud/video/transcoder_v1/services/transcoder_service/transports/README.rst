
transport inheritance structure
_______________________________

``TranscoderServiceTransport`` is the ABC for all transports.

- public child ``TranscoderServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TranscoderServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTranscoderServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TranscoderServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
