
transport inheritance structure
_______________________________

``ManagedKafkaConnectTransport`` is the ABC for all transports.

- public child ``ManagedKafkaConnectGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ManagedKafkaConnectGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseManagedKafkaConnectRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ManagedKafkaConnectRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
