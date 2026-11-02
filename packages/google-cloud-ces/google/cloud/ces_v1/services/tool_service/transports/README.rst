
transport inheritance structure
_______________________________

``ToolServiceTransport`` is the ABC for all transports.

- public child ``ToolServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ToolServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseToolServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ToolServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
