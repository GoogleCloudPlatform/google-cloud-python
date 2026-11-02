
transport inheritance structure
_______________________________

``ServiceManagerTransport`` is the ABC for all transports.

- public child ``ServiceManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ServiceManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseServiceManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ServiceManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
