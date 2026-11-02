
transport inheritance structure
_______________________________

``UptimeCheckServiceTransport`` is the ABC for all transports.

- public child ``UptimeCheckServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``UptimeCheckServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseUptimeCheckServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``UptimeCheckServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
