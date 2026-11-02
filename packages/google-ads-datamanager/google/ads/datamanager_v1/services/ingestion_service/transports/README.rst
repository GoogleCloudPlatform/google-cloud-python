
transport inheritance structure
_______________________________

``IngestionServiceTransport`` is the ABC for all transports.

- public child ``IngestionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IngestionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIngestionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IngestionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
