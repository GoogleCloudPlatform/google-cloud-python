
transport inheritance structure
_______________________________

``CreativeSetServiceTransport`` is the ABC for all transports.

- public child ``CreativeSetServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CreativeSetServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCreativeSetServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CreativeSetServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
