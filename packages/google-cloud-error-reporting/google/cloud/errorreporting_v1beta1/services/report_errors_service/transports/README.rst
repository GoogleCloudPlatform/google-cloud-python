
transport inheritance structure
_______________________________

``ReportErrorsServiceTransport`` is the ABC for all transports.

- public child ``ReportErrorsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReportErrorsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReportErrorsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReportErrorsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
