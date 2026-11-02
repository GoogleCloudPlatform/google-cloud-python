
transport inheritance structure
_______________________________

``AccountTaxServiceTransport`` is the ABC for all transports.

- public child ``AccountTaxServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AccountTaxServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAccountTaxServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AccountTaxServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
