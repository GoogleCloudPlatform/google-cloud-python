
transport inheritance structure
_______________________________

``GeneratorEvaluationsTransport`` is the ABC for all transports.

- public child ``GeneratorEvaluationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GeneratorEvaluationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGeneratorEvaluationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GeneratorEvaluationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
