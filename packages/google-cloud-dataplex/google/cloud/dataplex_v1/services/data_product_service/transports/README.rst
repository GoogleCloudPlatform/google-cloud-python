
transport inheritance structure
_______________________________

``DataProductServiceTransport`` is the ABC for all transports.

- public child ``DataProductServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataProductServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataProductServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataProductServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
