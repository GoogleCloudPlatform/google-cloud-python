
transport inheritance structure
_______________________________

``MemorystoreTransport`` is the ABC for all transports.

- public child ``MemorystoreGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MemorystoreGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMemorystoreRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MemorystoreRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
