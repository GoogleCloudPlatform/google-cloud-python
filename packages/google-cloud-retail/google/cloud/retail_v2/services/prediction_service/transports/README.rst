
transport inheritance structure
_______________________________

``PredictionServiceTransport`` is the ABC for all transports.

- public child ``PredictionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PredictionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePredictionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PredictionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
