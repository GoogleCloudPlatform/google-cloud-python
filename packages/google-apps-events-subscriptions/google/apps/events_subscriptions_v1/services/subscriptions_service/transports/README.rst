
transport inheritance structure
_______________________________

``SubscriptionsServiceTransport`` is the ABC for all transports.

- public child ``SubscriptionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SubscriptionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSubscriptionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SubscriptionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
