
transport inheritance structure
_______________________________

``SchemaServiceTransport`` is the ABC for all transports.

- public child ``SchemaServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SchemaServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSchemaServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SchemaServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
