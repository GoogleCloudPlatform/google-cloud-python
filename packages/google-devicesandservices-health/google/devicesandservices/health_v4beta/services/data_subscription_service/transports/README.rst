
transport inheritance structure
_______________________________

``DataSubscriptionServiceTransport`` is the ABC for all transports.

- public child ``DataSubscriptionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataSubscriptionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataSubscriptionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataSubscriptionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
