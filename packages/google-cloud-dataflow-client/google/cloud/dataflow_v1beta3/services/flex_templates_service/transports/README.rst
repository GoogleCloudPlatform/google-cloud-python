
transport inheritance structure
_______________________________

``FlexTemplatesServiceTransport`` is the ABC for all transports.

- public child ``FlexTemplatesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FlexTemplatesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFlexTemplatesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FlexTemplatesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
