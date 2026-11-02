
transport inheritance structure
_______________________________

``AutokeyAdminTransport`` is the ABC for all transports.

- public child ``AutokeyAdminGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AutokeyAdminGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAutokeyAdminRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AutokeyAdminRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
