
transport inheritance structure
_______________________________

``ProgrammaticBuyerServiceTransport`` is the ABC for all transports.

- public child ``ProgrammaticBuyerServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ProgrammaticBuyerServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseProgrammaticBuyerServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ProgrammaticBuyerServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
