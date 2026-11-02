
transport inheritance structure
_______________________________

``FleetRoutingTransport`` is the ABC for all transports.

- public child ``FleetRoutingGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FleetRoutingGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFleetRoutingRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FleetRoutingRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
