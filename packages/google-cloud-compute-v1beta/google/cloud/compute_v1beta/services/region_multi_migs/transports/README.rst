
transport inheritance structure
_______________________________

``RegionMultiMigsTransport`` is the ABC for all transports.

- public child ``RegionMultiMigsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegionMultiMigsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegionMultiMigsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegionMultiMigsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
