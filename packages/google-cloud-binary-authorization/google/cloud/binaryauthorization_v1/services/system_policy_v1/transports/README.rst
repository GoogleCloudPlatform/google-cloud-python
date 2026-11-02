
transport inheritance structure
_______________________________

``SystemPolicyV1Transport`` is the ABC for all transports.

- public child ``SystemPolicyV1GrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SystemPolicyV1GrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSystemPolicyV1RestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SystemPolicyV1RestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
