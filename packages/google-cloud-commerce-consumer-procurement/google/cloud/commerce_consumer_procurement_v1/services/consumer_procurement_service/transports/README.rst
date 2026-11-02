
transport inheritance structure
_______________________________

``ConsumerProcurementServiceTransport`` is the ABC for all transports.

- public child ``ConsumerProcurementServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConsumerProcurementServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConsumerProcurementServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConsumerProcurementServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
