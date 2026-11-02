
transport inheritance structure
_______________________________

``GbpAccountsServiceTransport`` is the ABC for all transports.

- public child ``GbpAccountsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GbpAccountsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGbpAccountsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GbpAccountsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
