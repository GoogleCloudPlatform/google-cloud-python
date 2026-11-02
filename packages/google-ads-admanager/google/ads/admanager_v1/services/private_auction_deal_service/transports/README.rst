
transport inheritance structure
_______________________________

``PrivateAuctionDealServiceTransport`` is the ABC for all transports.

- public child ``PrivateAuctionDealServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PrivateAuctionDealServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePrivateAuctionDealServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PrivateAuctionDealServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
