
transport inheritance structure
_______________________________

``SpacesServiceTransport`` is the ABC for all transports.

- public child ``SpacesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SpacesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSpacesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SpacesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
