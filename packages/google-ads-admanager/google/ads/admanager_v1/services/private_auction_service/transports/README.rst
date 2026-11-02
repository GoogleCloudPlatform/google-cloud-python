
transport inheritance structure
_______________________________

``PrivateAuctionServiceTransport`` is the ABC for all transports.

- public child ``PrivateAuctionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PrivateAuctionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePrivateAuctionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PrivateAuctionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
