
transport inheritance structure
_______________________________

``TestCasesTransport`` is the ABC for all transports.

- public child ``TestCasesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TestCasesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTestCasesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TestCasesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
