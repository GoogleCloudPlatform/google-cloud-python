
transport inheritance structure
_______________________________

``BigQueryExportServiceTransport`` is the ABC for all transports.

- public child ``BigQueryExportServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BigQueryExportServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBigQueryExportServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BigQueryExportServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
