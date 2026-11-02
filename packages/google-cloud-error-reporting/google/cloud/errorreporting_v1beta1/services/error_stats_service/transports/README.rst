
transport inheritance structure
_______________________________

``ErrorStatsServiceTransport`` is the ABC for all transports.

- public child ``ErrorStatsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ErrorStatsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseErrorStatsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ErrorStatsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
