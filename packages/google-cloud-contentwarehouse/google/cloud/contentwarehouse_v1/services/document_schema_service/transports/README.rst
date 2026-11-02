
transport inheritance structure
_______________________________

``DocumentSchemaServiceTransport`` is the ABC for all transports.

- public child ``DocumentSchemaServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DocumentSchemaServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDocumentSchemaServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DocumentSchemaServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
