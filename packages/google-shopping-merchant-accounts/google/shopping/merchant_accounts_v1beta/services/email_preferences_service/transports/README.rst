
transport inheritance structure
_______________________________

``EmailPreferencesServiceTransport`` is the ABC for all transports.

- public child ``EmailPreferencesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``EmailPreferencesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseEmailPreferencesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``EmailPreferencesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
