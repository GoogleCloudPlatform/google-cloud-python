
transport inheritance structure
_______________________________

``EvaluationServiceTransport`` is the ABC for all transports.

- public child ``EvaluationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EvaluationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEvaluationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EvaluationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
