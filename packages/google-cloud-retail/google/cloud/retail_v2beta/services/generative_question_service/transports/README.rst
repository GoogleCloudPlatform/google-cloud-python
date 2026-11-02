
transport inheritance structure
_______________________________

``GenerativeQuestionServiceTransport`` is the ABC for all transports.

- public child ``GenerativeQuestionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GenerativeQuestionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGenerativeQuestionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GenerativeQuestionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
