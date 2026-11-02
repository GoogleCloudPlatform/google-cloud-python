
transport inheritance structure
_______________________________

``InterconnectGroupsTransport`` is the ABC for all transports.

- public child ``InterconnectGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InterconnectGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInterconnectGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InterconnectGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
