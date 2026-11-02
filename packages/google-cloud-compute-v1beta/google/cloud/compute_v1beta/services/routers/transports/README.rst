
transport inheritance structure
_______________________________

``RoutersTransport`` is the ABC for all transports.

- public child ``RoutersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RoutersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRoutersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RoutersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
