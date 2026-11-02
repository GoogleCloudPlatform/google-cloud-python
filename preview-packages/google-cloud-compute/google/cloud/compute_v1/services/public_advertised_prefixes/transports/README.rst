
transport inheritance structure
_______________________________

``PublicAdvertisedPrefixesTransport`` is the ABC for all transports.

- public child ``PublicAdvertisedPrefixesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PublicAdvertisedPrefixesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePublicAdvertisedPrefixesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PublicAdvertisedPrefixesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
