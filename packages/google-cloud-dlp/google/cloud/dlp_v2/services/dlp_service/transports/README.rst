
transport inheritance structure
_______________________________

``DlpServiceTransport`` is the ABC for all transports.

- public child ``DlpServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DlpServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDlpServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DlpServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
