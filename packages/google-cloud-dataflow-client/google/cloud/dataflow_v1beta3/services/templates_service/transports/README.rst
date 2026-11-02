
transport inheritance structure
_______________________________

``TemplatesServiceTransport`` is the ABC for all transports.

- public child ``TemplatesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TemplatesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTemplatesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TemplatesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
