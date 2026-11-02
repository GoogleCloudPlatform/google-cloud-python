
transport inheritance structure
_______________________________

``BigQueryWriteTransport`` is the ABC for all transports.

- public child ``BigQueryWriteGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BigQueryWriteGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBigQueryWriteRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BigQueryWriteRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
