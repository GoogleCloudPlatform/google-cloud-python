
transport inheritance structure
_______________________________

``LineItemTemplateServiceTransport`` is the ABC for all transports.

- public child ``LineItemTemplateServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LineItemTemplateServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLineItemTemplateServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LineItemTemplateServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
