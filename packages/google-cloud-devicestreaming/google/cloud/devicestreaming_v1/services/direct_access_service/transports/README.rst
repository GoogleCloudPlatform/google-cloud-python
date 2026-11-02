
transport inheritance structure
_______________________________

``DirectAccessServiceTransport`` is the ABC for all transports.

- public child ``DirectAccessServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DirectAccessServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDirectAccessServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DirectAccessServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
