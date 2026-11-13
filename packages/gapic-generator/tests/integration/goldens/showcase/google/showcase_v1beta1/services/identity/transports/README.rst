
transport inheritance structure
_______________________________

``IdentityTransport`` is the ABC for all transports.

- public child ``IdentityGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IdentityGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIdentityRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IdentityRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
