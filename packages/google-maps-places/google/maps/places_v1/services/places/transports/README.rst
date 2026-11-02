
transport inheritance structure
_______________________________

``PlacesTransport`` is the ABC for all transports.

- public child ``PlacesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PlacesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePlacesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PlacesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
