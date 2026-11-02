
transport inheritance structure
_______________________________

``AnswerRecordsTransport`` is the ABC for all transports.

- public child ``AnswerRecordsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AnswerRecordsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAnswerRecordsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AnswerRecordsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
