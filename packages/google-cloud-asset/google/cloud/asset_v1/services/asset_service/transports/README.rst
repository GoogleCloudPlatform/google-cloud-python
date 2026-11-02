
transport inheritance structure
_______________________________

``AssetServiceTransport`` is the ABC for all transports.

- public child ``AssetServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AssetServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAssetServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AssetServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
