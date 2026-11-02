
transport inheritance structure
_______________________________

``LustreTransport`` is the ABC for all transports.

- public child ``LustreGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LustreGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLustreRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LustreRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
