
transport inheritance structure
_______________________________

``PrivilegedAccessManagerTransport`` is the ABC for all transports.

- public child ``PrivilegedAccessManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PrivilegedAccessManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePrivilegedAccessManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PrivilegedAccessManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
