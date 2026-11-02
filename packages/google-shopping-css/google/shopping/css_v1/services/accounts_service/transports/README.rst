
transport inheritance structure
_______________________________

``AccountsServiceTransport`` is the ABC for all transports.

- public child ``AccountsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AccountsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAccountsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AccountsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
