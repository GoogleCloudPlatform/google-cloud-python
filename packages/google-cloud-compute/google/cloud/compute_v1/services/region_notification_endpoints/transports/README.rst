
transport inheritance structure
_______________________________

``RegionNotificationEndpointsTransport`` is the ABC for all transports.

- public child ``RegionNotificationEndpointsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionNotificationEndpointsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionNotificationEndpointsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionNotificationEndpointsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
