
transport inheritance structure
_______________________________

``IAMTransport`` is the ABC for all transports.

- public child ``IAMGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IAMGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIAMRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IAMRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
