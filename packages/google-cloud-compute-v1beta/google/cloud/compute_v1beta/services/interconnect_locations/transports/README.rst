
transport inheritance structure
_______________________________

``InterconnectLocationsTransport`` is the ABC for all transports.

- public child ``InterconnectLocationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InterconnectLocationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInterconnectLocationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InterconnectLocationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
