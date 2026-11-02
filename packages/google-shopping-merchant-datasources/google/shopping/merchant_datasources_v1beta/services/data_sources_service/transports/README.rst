
transport inheritance structure
_______________________________

``DataSourcesServiceTransport`` is the ABC for all transports.

- public child ``DataSourcesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataSourcesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataSourcesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataSourcesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
