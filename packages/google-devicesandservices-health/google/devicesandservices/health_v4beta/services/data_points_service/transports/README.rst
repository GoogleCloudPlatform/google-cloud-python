
transport inheritance structure
_______________________________

``DataPointsServiceTransport`` is the ABC for all transports.

- public child ``DataPointsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataPointsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataPointsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataPointsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
