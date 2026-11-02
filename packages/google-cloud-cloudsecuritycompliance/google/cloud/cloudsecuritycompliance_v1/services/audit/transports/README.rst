
transport inheritance structure
_______________________________

``AuditTransport`` is the ABC for all transports.

- public child ``AuditGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AuditGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAuditRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AuditRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
