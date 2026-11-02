
transport inheritance structure
_______________________________

``IAMCredentialsTransport`` is the ABC for all transports.

- public child ``IAMCredentialsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IAMCredentialsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIAMCredentialsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IAMCredentialsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
