
transport inheritance structure
_______________________________

``IamCheckerTransport`` is the ABC for all transports.

- public child ``IamCheckerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IamCheckerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIamCheckerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IamCheckerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
