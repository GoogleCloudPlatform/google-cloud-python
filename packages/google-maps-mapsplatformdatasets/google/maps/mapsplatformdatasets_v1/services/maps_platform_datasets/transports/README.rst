
transport inheritance structure
_______________________________

``MapsPlatformDatasetsTransport`` is the ABC for all transports.

- public child ``MapsPlatformDatasetsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MapsPlatformDatasetsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMapsPlatformDatasetsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MapsPlatformDatasetsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
