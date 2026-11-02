
transport inheritance structure
_______________________________

``AuditManagerTransport`` is the ABC for all transports.

- public child ``AuditManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AuditManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAuditManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AuditManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
