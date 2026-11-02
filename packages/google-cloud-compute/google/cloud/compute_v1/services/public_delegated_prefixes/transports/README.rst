
transport inheritance structure
_______________________________

``PublicDelegatedPrefixesTransport`` is the ABC for all transports.

- public child ``PublicDelegatedPrefixesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PublicDelegatedPrefixesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePublicDelegatedPrefixesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PublicDelegatedPrefixesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
