
transport inheritance structure
_______________________________

``DaiAuthenticationKeyServiceTransport`` is the ABC for all transports.

- public child ``DaiAuthenticationKeyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DaiAuthenticationKeyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDaiAuthenticationKeyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DaiAuthenticationKeyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
