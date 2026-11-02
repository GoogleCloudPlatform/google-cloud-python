
transport inheritance structure
_______________________________

``ModelArmorTransport`` is the ABC for all transports.

- public child ``ModelArmorGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ModelArmorGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseModelArmorRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ModelArmorRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
