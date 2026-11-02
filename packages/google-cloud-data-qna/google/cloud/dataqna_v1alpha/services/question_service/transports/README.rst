
transport inheritance structure
_______________________________

``QuestionServiceTransport`` is the ABC for all transports.

- public child ``QuestionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``QuestionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseQuestionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``QuestionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
