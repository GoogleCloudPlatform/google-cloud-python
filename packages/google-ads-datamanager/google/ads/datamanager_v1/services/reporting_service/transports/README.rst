
transport inheritance structure
_______________________________

``ReportingServiceTransport`` is the ABC for all transports.

- public child ``ReportingServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReportingServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReportingServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReportingServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
