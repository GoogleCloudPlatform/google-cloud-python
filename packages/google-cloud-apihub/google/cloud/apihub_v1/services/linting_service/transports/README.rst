
transport inheritance structure
_______________________________

``LintingServiceTransport`` is the ABC for all transports.

- public child ``LintingServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LintingServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLintingServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LintingServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
