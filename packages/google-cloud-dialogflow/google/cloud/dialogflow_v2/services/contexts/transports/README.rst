
transport inheritance structure
_______________________________

``ContextsTransport`` is the ABC for all transports.

- public child ``ContextsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ContextsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseContextsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ContextsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
