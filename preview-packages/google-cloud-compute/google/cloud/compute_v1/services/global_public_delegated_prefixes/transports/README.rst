
transport inheritance structure
_______________________________

``GlobalPublicDelegatedPrefixesTransport`` is the ABC for all transports.

- public child ``GlobalPublicDelegatedPrefixesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalPublicDelegatedPrefixesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalPublicDelegatedPrefixesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalPublicDelegatedPrefixesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
