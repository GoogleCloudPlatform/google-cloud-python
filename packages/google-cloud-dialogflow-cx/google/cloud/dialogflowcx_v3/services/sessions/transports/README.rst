
transport inheritance structure
_______________________________

``SessionsTransport`` is the ABC for all transports.

- public child ``SessionsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SessionsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSessionsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SessionsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
