
transport inheritance structure
_______________________________

``SubscriberTransport`` is the ABC for all transports.

- public child ``SubscriberGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SubscriberGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSubscriberRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SubscriberRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
