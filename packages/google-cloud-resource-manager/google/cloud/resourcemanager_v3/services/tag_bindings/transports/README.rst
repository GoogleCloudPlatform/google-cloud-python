
transport inheritance structure
_______________________________

``TagBindingsTransport`` is the ABC for all transports.

- public child ``TagBindingsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TagBindingsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTagBindingsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TagBindingsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
