
transport inheritance structure
_______________________________

``FeedsServiceTransport`` is the ABC for all transports.

- public child ``FeedsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FeedsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFeedsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FeedsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
