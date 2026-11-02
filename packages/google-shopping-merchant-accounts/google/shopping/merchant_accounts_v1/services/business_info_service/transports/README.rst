
transport inheritance structure
_______________________________

``BusinessInfoServiceTransport`` is the ABC for all transports.

- public child ``BusinessInfoServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BusinessInfoServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBusinessInfoServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BusinessInfoServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
