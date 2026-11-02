
transport inheritance structure
_______________________________

``SupportEventSubscriptionServiceTransport`` is the ABC for all transports.

- public child ``SupportEventSubscriptionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SupportEventSubscriptionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSupportEventSubscriptionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SupportEventSubscriptionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
