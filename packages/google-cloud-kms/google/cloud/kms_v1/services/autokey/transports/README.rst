
transport inheritance structure
_______________________________

``AutokeyTransport`` is the ABC for all transports.

- public child ``AutokeyGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AutokeyGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAutokeyRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AutokeyRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
