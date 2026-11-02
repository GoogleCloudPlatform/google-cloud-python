
transport inheritance structure
_______________________________

``RegionInstanceTemplatesTransport`` is the ABC for all transports.

- public child ``RegionInstanceTemplatesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionInstanceTemplatesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionInstanceTemplatesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionInstanceTemplatesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
