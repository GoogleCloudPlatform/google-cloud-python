
transport inheritance structure
_______________________________

``StreamingServiceTransport`` is the ABC for all transports.

- public child ``StreamingServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``StreamingServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseStreamingServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``StreamingServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
