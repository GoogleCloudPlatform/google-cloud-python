
transport inheritance structure
_______________________________

``AzureClustersTransport`` is the ABC for all transports.

- public child ``AzureClustersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AzureClustersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAzureClustersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AzureClustersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
