
transport inheritance structure
_______________________________

``McmEarningsServiceTransport`` is the ABC for all transports.

- public child ``McmEarningsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``McmEarningsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMcmEarningsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``McmEarningsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
