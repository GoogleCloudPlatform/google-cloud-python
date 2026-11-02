
transport inheritance structure
_______________________________

``NetworkProfilesTransport`` is the ABC for all transports.

- public child ``NetworkProfilesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NetworkProfilesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNetworkProfilesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NetworkProfilesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
