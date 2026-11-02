
transport inheritance structure
_______________________________

``RetrieverServiceTransport`` is the ABC for all transports.

- public child ``RetrieverServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RetrieverServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRetrieverServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RetrieverServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
