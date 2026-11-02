
transport inheritance structure
_______________________________

``DataObjectSearchServiceTransport`` is the ABC for all transports.

- public child ``DataObjectSearchServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataObjectSearchServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataObjectSearchServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataObjectSearchServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
