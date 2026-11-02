
transport inheritance structure
_______________________________

``LoyaltyCustomerMatchServiceTransport`` is the ABC for all transports.

- public child ``LoyaltyCustomerMatchServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LoyaltyCustomerMatchServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLoyaltyCustomerMatchServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LoyaltyCustomerMatchServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
