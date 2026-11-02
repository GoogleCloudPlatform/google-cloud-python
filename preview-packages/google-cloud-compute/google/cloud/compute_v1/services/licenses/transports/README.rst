
transport inheritance structure
_______________________________

``LicensesTransport`` is the ABC for all transports.

- public child ``LicensesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LicensesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLicensesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LicensesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
