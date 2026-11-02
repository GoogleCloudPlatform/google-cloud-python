
transport inheritance structure
_______________________________

``DeliveryServiceTransport`` is the ABC for all transports.

- public child ``DeliveryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DeliveryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDeliveryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DeliveryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
