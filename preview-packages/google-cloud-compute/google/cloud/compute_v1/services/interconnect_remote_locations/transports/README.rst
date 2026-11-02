
transport inheritance structure
_______________________________

``InterconnectRemoteLocationsTransport`` is the ABC for all transports.

- public child ``InterconnectRemoteLocationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InterconnectRemoteLocationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInterconnectRemoteLocationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InterconnectRemoteLocationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
