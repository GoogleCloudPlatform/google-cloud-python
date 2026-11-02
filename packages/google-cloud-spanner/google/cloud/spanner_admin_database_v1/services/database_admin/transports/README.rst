
transport inheritance structure
_______________________________

``DatabaseAdminTransport`` is the ABC for all transports.

- public child ``DatabaseAdminGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DatabaseAdminGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDatabaseAdminRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DatabaseAdminRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
