
transport inheritance structure
_______________________________

``DataObjectServiceTransport`` is the ABC for all transports.

- public child ``DataObjectServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataObjectServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataObjectServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataObjectServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
