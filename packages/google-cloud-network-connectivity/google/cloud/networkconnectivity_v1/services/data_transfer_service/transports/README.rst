
transport inheritance structure
_______________________________

``DataTransferServiceTransport`` is the ABC for all transports.

- public child ``DataTransferServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataTransferServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataTransferServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataTransferServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
