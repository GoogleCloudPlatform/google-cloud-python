
transport inheritance structure
_______________________________

``PolicyBindingsTransport`` is the ABC for all transports.

- public child ``PolicyBindingsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PolicyBindingsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePolicyBindingsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PolicyBindingsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
