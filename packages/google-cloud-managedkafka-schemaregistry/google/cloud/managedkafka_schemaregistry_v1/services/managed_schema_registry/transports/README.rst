
transport inheritance structure
_______________________________

``ManagedSchemaRegistryTransport`` is the ABC for all transports.

- public child ``ManagedSchemaRegistryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ManagedSchemaRegistryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseManagedSchemaRegistryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ManagedSchemaRegistryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
