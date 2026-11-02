
transport inheritance structure
_______________________________

``DepServiceTransport`` is the ABC for all transports.

- public child ``DepServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DepServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDepServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DepServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
