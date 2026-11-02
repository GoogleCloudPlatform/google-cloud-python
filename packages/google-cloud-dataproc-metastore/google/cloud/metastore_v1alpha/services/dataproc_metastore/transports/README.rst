
transport inheritance structure
_______________________________

``DataprocMetastoreTransport`` is the ABC for all transports.

- public child ``DataprocMetastoreGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataprocMetastoreGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataprocMetastoreRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataprocMetastoreRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
