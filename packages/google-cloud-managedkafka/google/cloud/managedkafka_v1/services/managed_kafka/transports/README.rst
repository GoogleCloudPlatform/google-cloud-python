
transport inheritance structure
_______________________________

``ManagedKafkaTransport`` is the ABC for all transports.

- public child ``ManagedKafkaGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ManagedKafkaGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseManagedKafkaRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ManagedKafkaRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
