
transport inheritance structure
_______________________________

``PublisherTransport`` is the ABC for all transports.

- public child ``PublisherGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PublisherGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePublisherRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PublisherRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
