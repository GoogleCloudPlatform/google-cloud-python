
transport inheritance structure
_______________________________

``IdentityAwareProxyOAuthServiceTransport`` is the ABC for all transports.

- public child ``IdentityAwareProxyOAuthServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IdentityAwareProxyOAuthServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIdentityAwareProxyOAuthServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IdentityAwareProxyOAuthServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
