
transport inheritance structure
_______________________________

``RegionOperationsTransport`` is the ABC for all transports.

- public child ``RegionOperationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionOperationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionOperationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionOperationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
