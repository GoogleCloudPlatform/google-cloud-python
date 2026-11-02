
transport inheritance structure
_______________________________

``ConversionSourcesServiceTransport`` is the ABC for all transports.

- public child ``ConversionSourcesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConversionSourcesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConversionSourcesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConversionSourcesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
