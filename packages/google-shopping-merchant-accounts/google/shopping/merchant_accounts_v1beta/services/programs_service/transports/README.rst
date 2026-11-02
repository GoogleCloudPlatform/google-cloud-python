
transport inheritance structure
_______________________________

``ProgramsServiceTransport`` is the ABC for all transports.

- public child ``ProgramsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ProgramsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseProgramsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ProgramsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
