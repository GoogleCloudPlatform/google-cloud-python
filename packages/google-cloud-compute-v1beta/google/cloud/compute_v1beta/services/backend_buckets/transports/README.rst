
transport inheritance structure
_______________________________

``BackendBucketsTransport`` is the ABC for all transports.

- public child ``BackendBucketsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BackendBucketsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBackendBucketsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BackendBucketsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
